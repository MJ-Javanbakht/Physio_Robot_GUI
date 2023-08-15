import canopen

# Start with creating a network representing one CAN bus
network = canopen.Network()

# Add some nodes with corresponding Object Dictionaries
node1 = canopen.RemoteNode(127, 'modules/canOpen/ASDA_A2_1042sub980_C.eds')
network.add_node(node1)

network.connect(bustype='socketcan', channel='can0')

def init_drive(node , network):
	node.nmt.state = 'PRE-OPERATIONAL'

	node.sdo['Modes of operation'].raw=1 #

	node.sdo['Controlword'].raw=128 #Clear_Error
	node.sdo['Controlword'].raw=0 #Switch_ON
	node.sdo['Controlword'].raw=6 #
	node.sdo['Controlword'].raw=7 # Init & Run
	node.sdo['Controlword'].raw=15#
	node.sdo['Controlword'].raw=63#
	node.sdo['Modes of operation'].raw=1
	# Read PDO configuration from node
	node.rpdo.read()
	node.tpdo.read()

	# Re-map TPDO[1]
	node.tpdo[1].clear()
	node.tpdo[1].add_variable('Position actual value')
	node.tpdo[1].add_variable('Statusword')
	node.tpdo[1].enabled = True
	# Save new PDO configuration to node
	node.tpdo[1].save()

	node.rpdo[1].clear()
	node.rpdo[1].add_variable('Target Position')
	node.rpdo[1].add_variable('Profile velocity')
	node.rpdo[1].add_variable('Profile acc')
	
	node.rpdo[1].enabled = True
	node.rpdo.save()

	#node.rpdo[1]['Target Position'].raw = 0
	#node.rpdo[1]['Profile velocity'].raw = 0
	node.rpdo[1].start(0.005)


init_drive(node1, network)

print("all nodes are initiated")

node1.nmt.state = 'OPERATIONAL'
tp = node1.tpdo[1]['Position actual value'].raw
print("pos: ", tp)
node1.rpdo[1]['Target Position'].raw = 1000
node1.rpdo[1]['Profile velocity'].raw= 1500
node1.rpdo[1]['Profile acc'].raw = 10
node1.sdo['Controlword'].raw = 31

while True:
	try:
		a = node1.tpdo[1]['Statusword'].raw
		b = node1.tpdo[1]['Position actual value'].raw
		print(b,end=' ')
	except KeyboardInterrupt:
		print("STOP!")
		node1.sdo['Controlword'].raw = 0
		network.disconnect()
		raise

