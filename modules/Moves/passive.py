import canopen
import csv
import time
import math

class Passive():

    Stop_Time_i, Set_i, F_i, Count_i, P_old, Run_Time_old, Time_I= [0, 0 , 0, 0, 300, 0,0]

    def singenerator(self, Time, Amp, Bias, Speed, Phase):
        pi = math.pi 
        Per = 4 * Amp/Speed
        Sine = Amp * math.sin((2*pi/Per) * self.Run_Time_old + Phase) + Bias
        # print(Sine)
        return Sine

    def Set_Rep(self, Rest_Time, Pos, maxROM, minROM, Input, Repeats_Desired, Sets_Desired):
        Time = int(round(time.time()))
        
        F_o = self.F_i
        Count_o = self.Count_i
        Set_o = self.Set_i
        Stop_Time_o = self.Stop_Time_i

        if minROM-2 < Pos and Pos < minROM+2:
            F_o=1
        elif maxROM-2 < Pos and Pos < maxROM+2:
            F_o=2

        if F_o==1 and self.F_i==2:
            Count_o = self.Count_i + 1

        if Count_o == Repeats_Desired:
            if self.Set_i < Sets_Desired:
                Set_o = self.Set_i + 1
                Count_o = 0
                Stop_Time_o = Time

        if Set_o >= Sets_Desired:
            Set_o = Sets_Desired


        if (self.Set_i >= Sets_Desired or (Time-self.Stop_Time_i) < Rest_Time):
            output=0
            self.Flag=1
        else:
            output=Input
            self.Flag=0

        self.F_i = F_o
        self.Count_i = Count_o
        self.Set_i = Set_o
        self.Stop_Time_i = Stop_Time_o

        return output

    def timerreset(self):
        Time_O = Time_I + 0.001

        if self.Flag == 1:
            Time_O = 0

        Time_I = Time_O
        return Time_O

    def IncrementalPController(self, error, P_max):
        P = self.P_old + 0.1

        if P >= P_max:
            P = P_max
        PID_Output = P * error
        self.P_old = P
        print("p: ", P)
        return PID_Output

    def safetyFunction(self, Time, Theta_Sat_Pos, Theta_Sat_Neg, Input, Theta):
        upperLimit = 1000
        lowerLimit = -1000
        Run_Time = self.Run_Time_old + 0.00001

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
        
        self.Run_Time_old=Run_Time
        return output

    def init_drive(self, node , network):
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

    def run(self, node, time, restTime, sets, repeats, minROM, maxROM, speed):
        node.sdo['Modes of operation'].raw=3 #Velocity Mode
        node.nmt.state = 'OPERATIONAL'
        Time = 0
        try:
            while True:
                Theta = node.tpdo[1]['Position actual value'].raw *(360 / (1280000 * 25))

                Amp = (maxROM - minROM)/2
                Bias = minROM
                Time, Phase = [Time + 1, math.pi / 2]
                #Force
                output = self.singenerator(Time, Amp, Bias, speed, Phase)
                
                # Rest_Time, Pos, ROM, Input, Repeats_Desired, Sets_Desired = [1, Theta, 90, output, 5, 5]
                output = self.Set_Rep(restTime, Theta, minROM, maxROM, Input, repeats, sets)

                error = output - Theta
                print(error)
                output = self.IncrementalPController(error, 500)

                Time, Theta_Sat_Pos, Theta_Sat_Neg, Input = [100, 10, -100, output]
                output = self.safetyFunction(Time, Theta_Sat_Pos, Theta_Sat_Neg, Input, Theta)

                # print("output: ", output)
                node.rpdo[1]['Target velocity'].raw = output
                time.sleep(0.001)

        except KeyboardInterrupt:
            print("STOP!")
            node.sdo['Controlword'].raw = 0
        finally:  
            node.rpdo[1]['Target velocity'].raw = 0
            node.sdo['Controlword'].raw = 0
            
    # with open("actualPosition.csv",'w') as f:
    #     w = csv.writer(f)
    #     for a in apos:
    #         w.writerow([a])
