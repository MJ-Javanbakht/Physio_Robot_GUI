import time

offset = -200000

def init_drive(node):
    node.sdo['Modes of operation'].raw= 6 #Homing Mode

    node.sdo['Home offset'].raw = offset
    node.sdo['Homing method'].raw = 2
    node.sdo['Homing speeds']['Speed during search for switch'].raw = 200
    node.sdo['Homing speeds']['Speed during search for zero'].raw = 50

def Home(node):
    init_drive(node)

    node.sdo['Controlword'].raw = 31
    print(f"Homing Started with offset {offset}.")
    status = [0]*15
    while status[2] != "1":
        status = node.sdo['Statusword'].raw 
        status = bin(status)
        status = status.split("b")
        status = status[1]
        status = "{:0>15}".format(status)
        # print(status[2])

    print("Homing Done!")
    time.sleep(0.02)
    print("Going to 0 pulse.")

    node.sdo['Modes of operation'].raw = 1
    node.sdo['Target Position'].raw = 0
    # node.sdo['Profile velocity'].raw = 200000
    pos = 1
    while pos != 0 :
        pos = node.sdo['Position actual value'].raw
        # print(pos)
    print("Target reached.")
