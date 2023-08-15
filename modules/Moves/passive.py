from tokenize import PseudoExtras
import canopen
import csv
import time
import math

Stop_Time_i, Set_i, F_i, Count_i, P_old, Run_Time_old, Time_I= [0, 0 , 0, 0, 300, 0,0]

def singenerator(Time, Amp, Bias, Speed, Phase):
    global Run_Time_old
    pi = math.pi 
    Per=4*Amp/Speed
    Sine = Amp * math.sin((2*pi/Per)*Run_Time_old+Phase) + Bias
    # print(Sine)
    return Sine

def Set_Rep(Rest_Time, Pos, ROM, Input, Repeats_Desired, Sets_Desired):
    Time = int(round(time.time()))

    global F_i, Count_i, Set_i, Stop_Time_i, Flag
    F_o=F_i
    Count_o=Count_i
    Set_o=Set_i
    Stop_Time_o=Stop_Time_i

    if -2<Pos and Pos<+2:
        F_o=1
    elif -ROM-2<Pos and Pos<-ROM+2:
        F_o=2


    if F_o==1 and F_i==2:
        Count_o=Count_i+1


    if Count_o == Repeats_Desired:
        if Set_i<Sets_Desired:
            Set_o=Set_i+1
            Count_o=0
            Stop_Time_o=Time

    if Set_o>=Sets_Desired:
        Set_o=Sets_Desired


    if (Set_i>=Sets_Desired or (Time-Stop_Time_i) < Rest_Time):
        output=0
        Flag=1
    else:
        output=Input
        Flag=0

    F_i = F_o
    Count_i = Count_o
    Set_i = Set_o
    Stop_Time_i = Stop_Time_o

    return output

def timerreset(Flag):
    Time_O = Time_I + 0.001

    if Flag == 1:
        Time_O = 0

    Time_I = Time_O
    return Time_O

def IncrementalPController(error, P_max):
    global P_old
    P = P_old + 0.1

    if P >= P_max:
        P = P_max
    PID_Output = P * error
    P_old = P
    print("p: ", P)
    return PID_Output

def safetyFunction(Time, Theta_Sat_Pos, Theta_Sat_Neg, Input, Theta):
    global Run_Time_old
    upperLimit = 1000
    lowerLimit = -1000
    Run_Time = Run_Time_old + 0.00001

    if Theta > Theta_Sat_Pos:
        output = 0
    elif Theta < Theta_Sat_Neg:
        output = 0
    else:
        output = Input


    if Run_Time > Time - 5:
        output = 0.01*(-Theta)
        
    if output > upperLimit:
        output = upperLimit
    elif output < lowerLimit:
        output = lowerLimit
    
    Run_Time_old=Run_Time
    return output

# Start with creating a network representing one CAN bus
network = canopen.Network()

# Add some nodes with corresponding Object Dictionaries
node1 = canopen.RemoteNode(1, 'ASDA_A2_1042sub980_C.eds')
network.add_node(node1)

network.connect(bustype='socketcan', channel='can0')


def init_drive(node , network):
  node.nmt.state = 'PRE-OPERATIONAL'
  node.sdo['Controlword'].raw=128 #Clear_Error
  node.sdo['Controlword'].raw=0 #Switch_ON
  node.sdo['Controlword'].raw=6 #
  node.sdo['Controlword'].raw=7 # Init & Run
  node.sdo['Controlword'].raw=15#

  node.sdo['Modes of operation'].raw=3 #output Mode

	# Read PDO configuration from node
  node.rpdo.read()
  node.tpdo.read()
	# Re-map TPDO[1]
  node.tpdo[1].clear()
  node.tpdo[1].add_variable('Position actual value')
  node.tpdo[1].add_variable('output actual value')
  node.tpdo[1].enabled = True

  # Re-map TPDO[2]
  node.tpdo[2].clear()
  node.tpdo[2].add_variable('Torque actual value')
  # node.tpdo[2].add_variable('output actual value')
  node.tpdo[2].enabled = True

	# Save new PDO configuration to node
  node.tpdo[1].save()
  node.tpdo[2].save()

  node.rpdo[1].clear()
  node.rpdo[1].add_variable('Target velocity')
  #node.rpdo[1].add_variable('Target velocity')
  node.rpdo[1].enabled = True
  node.rpdo.save()
  node.rpdo[1].start(0.005)

init_drive(node1, network)
print("all nodes are initiated")

node1.nmt.state = 'OPERATIONAL'
Time = 0
try:
  while True:
    Theta = node1.tpdo[1]['Position actual value'].raw *(360 / (1280000 * 25))

    Time, Amp, Bias, Speed, Phase = [Time + 1, 45, -45, 1000, math.pi / 2]
    #Force
    output = singenerator(Time, Amp, Bias, Speed, Phase)
     
    Rest_Time, Pos, ROM, Input, Repeats_Desired, Sets_Desired = [1, Theta, 90, output, 5, 5]
    output = Set_Rep(Rest_Time, Pos, ROM, Input, Repeats_Desired, Sets_Desired)

    error = output - Theta
    print(error)
    output = IncrementalPController(error, 500)

    Time, Theta_Sat_Pos, Theta_Sat_Neg, Input = [100, 10, -100, output]
    output = safetyFunction(Time, Theta_Sat_Pos, Theta_Sat_Neg, Input, Theta)

    # print("output: ", output)
    node1.rpdo[1]['Target velocity'].raw = output
    time.sleep(0.001)

except KeyboardInterrupt:
    print("STOP!")
    node1.sdo['Controlword'].raw = 0
    network.disconnect()
finally:  
    node1.rpdo[1]['Target velocity'].raw = 0
    node1.sdo['Controlword'].raw = 0
    network.disconnect()
        
# with open("actualPosition.csv",'w') as f:
#     w = csv.writer(f)
#     for a in apos:
#         w.writerow([a])
