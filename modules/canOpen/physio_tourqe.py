import canopen
import time
import math
# Start with creating a network representing one CAN bus
network = canopen.Network()

# Add some nodes with corresponding Object Dictionaries
node1 = canopen.RemoteNode(127, 'modules/canOpen/ASDA_A2_1042sub980_C.eds')
network.add_node(node1)

network.connect(bustype='socketcan', channel='can0')

def init_drive(node , network):
	node.nmt.state = 'PRE-OPERATIONAL'
	time.sleep(1)
	node.sdo['Modes of operation'].raw=4 #Torque Mode

	node.sdo['Controlword'].raw=128 #Clear_Error
	node.sdo['Controlword'].raw=0 #Switch_ON
	node.sdo['Controlword'].raw=6 #
	node.sdo['Controlword'].raw=7 # Init & Run
	node.sdo['Controlword'].raw=15#

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
	node.rpdo[1].add_variable('Target torque')
	node.rpdo[1].enabled = True
	node.rpdo.save()

	#node.rpdo[1]['target_position_b'].raw = 0
	#node.rpdo[1]['profile_velocity_b'].raw = 0
	node.rpdo[1].start(0.001)


init_drive(node1, network)

print("all nodes are initiated")

node1.nmt.state = 'OPERATIONAL'

node1.rpdo[1]['Target torque'].raw = -50
t = 0
while True:
	#cpw = node.tpdo[1]["Position actual value"].raw
	#print(cpw)
	t = t + 1 
	#tqe = 50 * math.sin(t/ 100.0)
	#node1.rpdo[1]['Target torque'].raw = tqe
	#time.sleep(0.001)
	

