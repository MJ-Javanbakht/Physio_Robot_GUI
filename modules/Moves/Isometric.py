import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from . loadcell import loadcell
from .. canOpen.config import *

class Isometric(QObject):
    finished = pyqtSignal()
    M_i, Timer_Hold, Timer_Rest, F_i, Counter_Repeat, Counter_Set, Run_Time_old = [0, 0, 0, 0, 0, 0, 0]
    Force = 0

    def Refrence_Generator(self, Force_Ref, Time_h, Theta1, Theta2, Theta3, Theta, Force):
        
        Velocity = 0
        # global M_i, Timer_Hold
        M_o = self.M_i
        Timer = self.Timer_Hold

        print('Holding Time = ',Timer)    #Timer for holding

        if Force_Ref < 0:
            Force=-Force
            Force_Ref=-Force_Ref

        if M_o == 0:
            Velocity = 0.01*(-Theta1 - Theta)
            if Force > Force_Ref and abs(-Theta1 - Theta) < 10:
                Timer = self.Timer_Hold + 0.03
            else:
                Timer = 0
            if Timer > Time_h:
                M_o = 1

        if M_o == 1:
            #Timer = 5
            Velocity = 0.01*(-Theta2 - Theta) 
            if Force > Force_Ref and abs(-Theta2 - Theta) < 10:
                Timer = self.Timer_Hold + 0.03
            else:
                Timer = 5
            if Timer > Time_h + 5:
                M_o = 2

        if M_o == 2:
            #Timer = 10
            Velocity = 0.01*(-Theta3 - Theta)
            if Force > Force_Ref and abs(-Theta3 - Theta) < 10:
                Timer = self.Timer_Hold + 0.03
            else:
                Timer = 10
            if Timer > Time_h + 10:
                M_o = 0
        self.Timer_Hold = Timer
        self.M_i = M_o
        return Velocity

    def Set_Rep(self, Rest_Time, Pos, Ti1, Ti2, Input, Repeats_Desired, Sets_Desired):        
        F_o = self.F_i
        Count_o = self.Counter_Repeat
        Set_o = self.Counter_Set

        if -Ti1-5<Pos and Pos<-Ti1+5:
            F_o = 1
        elif -Ti2-5<Pos and Pos<-Ti2+5:
            F_o = 2

        if F_o == 1 and self.F_i == 2:
            Count_o = self.Counter_Repeat+1

        if Count_o == Repeats_Desired:
            if self.Counter_Set < Sets_Desired:
                Set_o = self.Counter_Set+1
            Count_o = 0
            self.Timer_Rest = 0
            
            
        print('Counter_Set = ',self.Counter_Set)
        if Set_o >= Sets_Desired:
            Set_o = Sets_Desired

        if (self.Counter_Set >= Sets_Desired or self.Timer_Rest < Rest_Time):
            self.Timer_Rest += 0.03
            if  self.Counter_Set >= Sets_Desired and -1 < Pos and Pos < 1:
                stop_while = 0
            Output = 0.01*(-Pos)
        else:
            Output = Input

        self.F_i = F_o
        self.Counter_Repeat = Count_o
        self.Counter_Set = Set_o

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

    def run(self, node, Rest_Time, Sets_Desired, Repeats_Desired, Force_Desired, Hold_Time, Theta1, Theta2, Theta3):        
        start(node, 0.005)
        setModesOfOperation(node, 3)

        try:
            while True:
                # Theta = node.tpdo[1]['Position actual value'].raw *(360 / (1280000 * 25))
                Theta = getPosition(node) * (360 / (1280000 * 25))
                print('Position:', Theta)
                self.Force = loadcell.return_loadcell()
                print("force:", self.Force)
                Velocity = self.Refrence_Generator(Force_Desired, Hold_Time, Theta1, Theta2, Theta3, Theta, self.Force)
                Velocity = self.Set_Rep(Rest_Time, Theta, Theta1, Theta2, Velocity, Repeats_Desired, Sets_Desired)
                # Time, Theta_Sat_Pos, Theta_Sat_Neg, Input = [100, 10, -80, Velocity]
                # Velocity = Safety_Function(Time, Theta_Sat_Pos, Theta_Sat_Neg, Input, Theta)
                
                print("Velocity:", Velocity)
                setTargetVelocity(node, Velocity * 5000)
                # node.rpdo[1]['Target velocity'].raw = Velocity * 5000
                # print('Loop Time = ',abs(LoopTime - time.time()))
                # LoopTime = time.time()

        except KeyboardInterrupt:
            print("STOP!")
        except Exception as e:
            print(e)
        finally:
            self.finished.emit()
            stop(node)

# with open("actualPosition.csv",'w') as f:
#     w = csv.writer(f)
#     for a in apos:
#         w.writerow([a])
