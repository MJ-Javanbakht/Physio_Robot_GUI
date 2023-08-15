class Tourqe():

	def init_drive(self, node):
		node.nmt.state = 'PRE-OPERATIONAL'

		node.sdo['Modes of operation'].raw=4 #Torque Mode

		node.sdo['Controlword'].raw=128 #Clear_Error
		node.sdo['Controlword'].raw=0 #Switch_ON
		node.sdo['Controlword'].raw=6 #
		node.sdo['Controlword'].raw=7 # Init & Run
		node.sdo['Controlword'].raw=15#

		# Set speed limit in rpm : 25 -> 1 
		node.sdo['P1-55'].raw = 25 * 10

		# Read PDO configuration from node
		node.rpdo.read()
		node.tpdo.read()

		# Re-map TPDO[1]
		node.tpdo[1].clear()
		node.tpdo[1].add_variable('Position actual value')
		node.tpdo[1].add_variable('Torque actual value')
		node.tpdo[1].enabled = True
		# Save new PDO configuration to node
		node.tpdo[1].save()
		
		# Re-map RPDO[1]
		node.rpdo[1].clear()
		node.rpdo[1].add_variable('Target torque')
		node.rpdo[1].enabled = True
		# Save new PDO configuration to node
		node.rpdo.save()	
		node.rpdo[1].start(0.001)

	def start(self, node):
		self.init_drive(node)
		print("node ", node, " initiated.")
		node.nmt.state = 'OPERATIONAL'
		print("node ", node, " is operational.")

	def stop(self, node, network):
		node.rpdo[1]['Target tourqe'].raw = 0
		node.sdo['Controlword'].raw = 0
		network.disconnect()
		print("network ", network, " disconnected.")

	def setTourqe(self, node, tor):
		node.rpdo[1]['Target tourqe'].raw = tor

	def getTourqe(self, node):
		return node.tpdo[1]['Tourqe actual value'].raw

	def getPosition(self, node):
		return node.tpdo[1]['Position actual value'].raw