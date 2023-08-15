import time

class Homing():
    offset = 0

    def init_drive(self, node):
        node.sdo['Modes of operation'].raw= 6 #Homing Mode

        node.sdo['Home offset'].raw = self.offset
        node.sdo['Homing method'].raw = 2
        node.sdo['Homing speeds']['Speed during search for switch'].raw = 200
        node.sdo['Homing speeds']['Speed during search for zero'].raw = 50

    def Home(self, node):
        self.init_drive(node)
        try:
            node.sdo['Controlword'].raw = 31
            print(f"Homing Started with offset {self.offset}.")
            status = [0]*15
            while status[2] != "1":
                status = node.sdo['Statusword'].raw 
                status = bin(status)
                status = status.split("b")
                status = status[1]
                status = "{:0>15}".format(status)
                # print(status[2])

            print("Homing Done!")
            time.sleep(0.2)
            print("Going to 0 pulse.")

            node.sdo['Modes of operation'].raw = 1
            tpos = 1000000
            node.rpdo[1]['Target Position'].raw = tpos
            node.rpdo[1]['Profile velocity'].raw = 200000
            time.sleep(1)
            pos = node.tpdo[1]['Position actual value'].raw
            print(tpos)
            time.sleep(1)
            while pos != tpos:
                time.sleep(0.01)
                pos = node.tpdo[1]['Position actual value'].raw
                print(pos)
            print("Target reached.")
        finally:
            node.sdo['Controlword'].raw = 0
