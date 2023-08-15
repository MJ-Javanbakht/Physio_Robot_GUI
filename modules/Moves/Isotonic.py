from tokenize import PseudoExtras
import canopen
import csv
import time
import math
import RPi.GPIO as GPIO
import keyboard  # using module keyboard
from pynput.keyboard import Listener
import Adafruit_ADS1x15

f_i, set_i, stopTime_i, count_d_i, count_u_i, runTime_old, state_i = 7*[0]
global theta
thetaG = 0
m = 3.2
g = 9.81
pi = math.pi 
deg2rad = pi/180 
force2torque = 29.55/100 #???
torque2voltage = 10/31.8 #???
Time = int(round(time.time()))

# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
# adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=5)
# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

# =================================================================
# =================================================================

def setRepFunc(position, ROM, extentionForce, flexionForce, setsDesired, repeatsDesired, restTime):
    
    global f_i, count_d_i, count_u_i, state_i, set_i, stopTime_i, repeats   # set_i and repeats also used in next
    f_o = f_i
    state_o = state_i
    count_d_o = count_d_i
    count_u_o = count_u_i
    set_o = set_i
    stopTime_o = stopTime_i
    time2 =  int(round(time.time())) - Time
    # position = -position   # me
    if position > 0:
        f_o = 1
    elif position <= 0 and position >= (-ROM + 5):
        f_o = 2
    elif position < (-ROM + 5):
        f_o = 3

    if (position <= 0 and position >= (-ROM + 5)) and (f_i == 1):
        state_o = 1
    elif (position < (-ROM + 5)) and (f_i == 2):
        state_o = 2
    elif (position <= 0 and position >= (-ROM + 5)) and (f_i == 3):
        state_o = 3
    elif (position > 0) and (f_i == 2):
        state_o = 4

    if state_o == 2 and state_i == 1:
        count_u_o = count_u_i + 1
    elif state_o == 4 and state_i == 3:
        count_d_o = count_d_i + 1
    
    repeats = math.floor((count_u_i + count_d_i)/2)

    if repeats == repeatsDesired:
        if set_i < setsDesired:
            set_o = set_i + 1
        count_u_o = 0
        count_d_o = 0
        stopTime_o = time2

    if set_o >= setsDesired:
        set_o = setsDesired    

    if ((set_i >= setsDesired) or (time2 - stopTime_i < restTime)):
        output = 0
    elif (state_i == 1 or state_i == 2):
        output = extentionForce
    elif (state_i == 3 or state_i == 4):
        output = flexionForce
    else:
        output = 0
    
    f_i = f_o
    state_i = state_o
    count_d_i = count_d_o
    count_u_i = count_u_o
    set_i = set_o
    stopTime_i = stopTime_o
    return output
# end def
# =================================================================

def safetyFunc(theta, thetaSatPositive, thetaSatNegative, velocity, forceRef):
    
    upperLimit = (7) * 15
    lowerLimit = (-7) * 15
    Ir = (m*g*math.sin((thetaSatPositive - 10)*deg2rad)+forceRef)*force2torque*torque2voltage
    Irmax = (5) * 10
    Irmin_p = (m*g*math.sin((-thetaSatNegative+10)*deg2rad)+forceRef)*force2torque*torque2voltage #???
    Irmin_n = (m*g*math.sin((-thetaSatNegative+20)*deg2rad)+forceRef)*force2torque*torque2voltage #???

    if forceRef >= 0:
        # Near Zero (10)
        if (theta > thetaSatPositive -10) and (theta < thetaSatPositive): #1
            output = forceRef#-forceRef/10 * (theta - thetaSatPositive) #(-Ir/10)*(theta - thetaSatPositive)
        elif theta > thetaSatPositive: #2
            output = 0
        # Near ROM (10)
        elif (theta > ((-thetaSatNegative)*(-1))) and (theta < ((-thetaSatNegative)*(-1)) + 10): #3
            output = forceRef #(((Irmin_p - Irmax)/10)*(theta+thetaSatNegative))+Irmax
        elif theta < (-thetaSatNegative) * (-1): #4
            output = forceRef #(5) * 10
        else: 
            output = forceRef  # voltage
        
    else:
        # Near Zero (10)
        if (theta > thetaSatPositive - 10) and (theta < thetaSatPositive):
            output = (-Ir/10)*(theta - thetaSatPositive)
        elif (theta > thetaSatPositive):
            output = 0
        # Near ROM (20)
        elif (theta > -thetaSatNegative) and (theta < -thetaSatNegative + 20):
            output = (((Irmin_n - Irmax)/20)*(theta+thetaSatNegative))+ Irmax
        elif theta < -thetaSatNegative:
            output = (5) * 10
        else:            
            output = forceRef         
    # outZero = forceCompensator(theta, velocity)
    # output += outZero 
    if output > upperLimit:
        output = upperLimit
    elif output < lowerLimit:
        output = lowerLimit
    return output
# end def
# =================================================================

def forceCompensator(theta, velocity):
    if theta < 0:
        if velocity < 0:
            output = 0.0084924 * (velocity * 0.0000002094) + 0.0043534 *  math.sin(theta*0.0000002094) + 24.0742 * -1
            # tTor= 0.020679 * (Acc * 0.0000002094) + 0.0084924 * (velocity * 0.0000002094) + 0.0043534 *  math.sin(pos*0.0000002094) + 24.0742 * np.sign(velocity)
        # elif np.sign(velocity) == 0 and t>1:
        #     node1.sdo['Controlword'].raw = 0
        #     network.disconnect()
        #     exit()
        else:
            output = 0.0084924 * (velocity * 0.0000002094) + 0.0043534 *  math.sin(theta*0.0000002094) + 28.0742 
            # tTor= 0.020679 * (Acc * 0.0000002094) + 0.0084924 * (velocity * 0.0000002094) + 0.0043534 *  math.sin(pos*0.0000002094) + 28.0742 * np.sign(velocity)
    else:
        output = 0
    return output
# end def
# =================================================================

def  weightCompensator(theta):
    output = m*g*math.sin(deg2rad*theta)
    return output    
# end def
# =================================================================

def force2voltageFunc(force):
    output = force * force2torque * torque2voltage  
    return output  
# end def
# =================================================================

def controllerSwitch(theta, time, fromSafety):
    global runTime_old, outS, outT
    runTime = runTime_old + 0.001
    if runTime > (time - 5):
        # run homeing mode
        # .
        # .
        # .
        # outS = 0.01 * (-theta)
        # outT = 5        
        pass
    else:
        outT = fromSafety
        outS = 1
    runTime_old = runTime
    return outS, outT
# end def
# =================================================================

def init_drive(node):
    node.sdo['Modes of operation'].raw=4 #Torque Mode
    node.nmt.state = 'OPERATIONAL'

# =================================================================

def run(node, restTime, setsDesired, repeatsDesired, extentionForce, flexionForce, minROM, maxROM):
    init_drive(node)
    init_drive(node)
    ROM = maxROM - minROM
    try:
        while set_i < setsDesired:
            theta = node.tpdo[1]['Position actual value'].raw *(360 / (1280000 * 25))
            vel = node.tpdo[1]['Velocity actual value'].raw * (60/250) 
            trq = node.tpdo[2]['Torque actual value'].raw * (7.16*25/1000)
            # Sets and Repeats >> Repeats - Sets - Force
            force_setRep = setRepFunc(theta, ROM, extentionForce, flexionForce, setsDesired, repeatsDesired, restTime)
            # weightCompensator >> compensating force
            # w_compensating = weightCompensator(theta)

            # force2voltage 
            # input_force2voltage = force_setRep + w_compensating
            # voltage = force2voltageFunc(input_force2voltage)
            # forceCompensating_T = forceCompensator(theta, vel)
            # safetyFunction 
            thetaSatPositive, thetaSatNegative = [0, -40]
            out_safetyFunc = safetyFunc(theta, thetaSatPositive, thetaSatNegative, vel, force_setRep)
            
            # controllerSwitch >> speed - torque
            # theta, time1, fromSafety = [thetaG, 100, out_safetyFunc]
            # [speedCommand, torqueCommand] = controllerSwitch(theta, time1, fromSafety)

            # node1.rpdo[1]['Target velocity'].raw = speedCommand
            node.rpdo[2]['Target torque'].raw = out_safetyFunc
            # print('TCommand : ' + str(torqueCommand) + ', SetRepeat_T : ' + 
            # str(force_setRep) + ', set : ' + str(set_i),'repeats : '+str(repeats))
            print('theta: ' + str(int(theta)) + ' ,actT : ' + str(int(trq)) + ' SetRep : ' + str(force_setRep) + 
            ', safety : ' + str(int(out_safetyFunc)) + ', set : ' + str(set_i),'repeats : '+str(repeats) ) #+ ', TCommand : ' + str(torqueCommand))
            # str(force_setRep))
            # time.sleep(0.005)

    except KeyboardInterrupt:
        print("STOP!")
        node.sdo['Controlword'].raw = 0
    finally:    
        node.rpdo[2]['Target velocity'].raw = 0
        node.sdo['Controlword'].raw = 0
