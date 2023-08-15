# import canopen
import time
import traceback
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import Adafruit_ADS1x15

class Isometric(QObject):
    finished = pyqtSignal()
    adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=5)
    M_i, Timer_i, F_i, Count_i, Set_i, Timer2, Run_Time_old = [0, 0, 0, 0, 0, 100, 0]

    def Force_Loadcell(self):
        GAIN = 1
        time.sleep(0.001)
        ADC_Value = (self.adc.read_adc(0, gain=GAIN, data_rate=860) - 19944)/6.232
        return ADC_Value

    def Refrence_Generator(self, Force_Ref, Time_h, Theta1, Theta2, Theta3, Theta, Force):
        
        Velocity = 0
        # global M_i, Timer_i
        M_o = self.M_i
        Timer = self.Timer_i

        print('Holding Time = ',Timer)    #Timer for holding

        if Force_Ref < 0:
            Force=-Force
            Force_Ref=-Force_Ref

        if M_o == 0:
            Velocity = 0.01*(-Theta1 - Theta)
            if Force > Force_Ref and abs(-Theta1 - Theta) < 10:
                Timer = self.Timer_i + 0.003
            else:
                Timer = 0
            if Timer > Time_h:
                M_o = 1

        if M_o == 1:
            #Timer = 5
            Velocity = 0.01*(-Theta2 - Theta) 
            if Force > Force_Ref and abs(-Theta2 - Theta) < 10:
                Timer = self.Timer_i + 0.003
            else:
                Timer = 5
            if Timer > Time_h + 5:
                M_o = 2

        if M_o == 2:
            #Timer = 10
            Velocity = 0.01*(-Theta3 - Theta)
            if Force > Force_Ref and abs(-Theta3 - Theta) < 10:
                Timer = self.Timer_i + 0.003
            else:
                Timer = 10
            if Timer > Time_h + 10:
                M_o = 0
        self.Timer_i = Timer
        self.M_i = M_o
        return Velocity

    def Set_Rep(self, Rest_Time, Pos, Ti2, Ti1, Input, Repeats_Desired, Sets_Desired):        
        F_o = self.F_i
        Count_o = self.Count_i
        Set_o = self.Set_i

        if -Ti1-5<Pos and Pos<-Ti1+5:
            F_o = 1
        elif -Ti2-5<Pos and Pos<-Ti2+5:
            F_o = 2

        if F_o == 1 and self.F_i == 2:
            Count_o = self.Count_i+1

        if Count_o == Repeats_Desired:
            if self.Set_i < Sets_Desired:
                Set_o = self.Set_i+1
            Count_o = 0
            self.Timer2 = 0
            
            
        print('set_i = ',self.Set_i)
        if Set_o >= Sets_Desired:
            Set_o = Sets_Desired

        if (self.Set_i >= Sets_Desired or self.Timer2 < Rest_Time):
            self.Timer2 += 0.003
            if  self.Set_i >= Sets_Desired and -1 < Pos and Pos < 1:
                stop_while = 0
            Output = 0.01*(-Pos)
        else:
            Output = Input

        self.F_i = F_o
        self.Count_i = Count_o
        self.Set_i = Set_o

        return Output

    def Safety_Function(self, Time, Theta_Sat_Pos, Theta_Sat_Neg, Input, Theta):
        Run_Time = self.Run_Time_old + 0.001
        if Theta > Theta_Sat_Pos:
            Output = 0
        elif Theta < Theta_Sat_Neg:
            Output = 0
        else:
            Output = Input

        if Run_Time > Time - 5:
            Output = 0.01*(-Theta)
        self.Run_Time_old = Run_Time

        return Output

    def init_drive(self, node):
        node.sdo['Modes of operation'].raw=3 #Velocity Mode

    def run(self, node, Rest_Time, Sets_Desired, Repeats_Desired, Force_Ref, Hold_Time, Theta1, Theta2, Theta3):
        node.sdo['Modes of operation'].raw=3 #Velocity Mode
        node.nmt.state = 'OPERATIONAL'

        while True:
            try:
                Theta = node.tpdo[1]['Position actual value'].raw *(360 / (1280000 * 25))
                Force = self.Force_Loadcell()
                Velocity = self.Refrence_Generator(Force_Ref, Hold_Time, Theta1, Theta2, Theta3, Theta, Force)
                Velocity = self.Set_Rep(Rest_Time, Theta, Theta2, Theta1, Velocity, Repeats_Desired, Sets_Desired)
                # print('Vel = ', Velocity)
                # Time, Theta_Sat_Pos, Theta_Sat_Neg, Input = [100, 10, -80, Velocity]
                # Velocity = Safety_Function(Time, Theta_Sat_Pos, Theta_Sat_Neg, Input, Theta)
                print("Velocity:     ", Velocity)
                node.rpdo[2]['Target velocity'].raw = Velocity * 1000

            except KeyboardInterrupt:
                print("STOP!")
                break
            except Exception as e:
                traceback.print_exc()
                continue
        # finally:
        node.rpdo[2]['Target velocity'].raw = 0
        node.sdo['Controlword'].raw = 0
