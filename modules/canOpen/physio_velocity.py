import canopen
import csv
import time
import math
import keyboard  # using module keyboard
from pynput.keyboard import Listener

# Start with creating a network representing one CAN bus
network = canopen.Network()

# Add some nodes with corresponding Object Dictionaries
node1 = canopen.RemoteNode(127, 'modules/canOpen/ASDA_A2_1042sub980_C.eds')
network.add_node(node1)

network.connect(bustype='socketcan', channel='can0')


def init_drive(node , network):
  node.nmt.state = 'PRE-OPERATIONAL'
  node.sdo['Controlword'].raw=128 #Clear_Error
  node.sdo['Controlword'].raw=0 #Switch_ON
  node.sdo['Controlword'].raw=6 #
  node.sdo['Controlword'].raw=7 # Init & Run
  node.sdo['Controlword'].raw=15#


  node.sdo['Modes of operation'].raw=3 #Velocity Mode

	# Read PDO configuration from node
  node.rpdo.read()
  node.tpdo.read()
	# Re-map TPDO[1]
  node.tpdo[1].clear()
  node.tpdo[1].add_variable('Position actual value')
  node.tpdo[1].enabled = True
	# Save new PDO configuration to node
  node.tpdo[1].save()
  node.rpdo[1].clear()
  node.rpdo[1].add_variable('Target velocity')
  node.rpdo[1].enabled = True
  node.rpdo.save()
  node.rpdo[1].start(0.005)

init_drive(node1, network)




print("all nodes are initiated")

node1.nmt.state = 'OPERATIONAL'


def stop():
    node1.rpdo[1]['Target velocity'].raw = 0
    #node1.rpdo[1]['Target velocity'].raw = 0
    #node1.sdo['Controlword'].raw = 0
    #network.disconnect()
    #exit()


#node2 a motor 3
#node1 a motor 1
#node1 b motor 2
def on_press(key):
    s = 1
    node1.rpdo[1]['Target velocity'].raw = 1500 * s
 
def on_release(key):

    stop()
    # Stop listener
    node1.rpdo[1]['Target velocity'].raw = 0
    node1.sdo['Controlword'].raw = 0
    network.disconnect()
    exit(0)

with Listener( on_press=on_press, on_release=on_release) as listener:
	listener.join()
