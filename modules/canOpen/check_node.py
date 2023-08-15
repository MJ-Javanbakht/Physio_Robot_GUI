import canopen
import time 

def check_node():
	network = canopen.Network()
	network.connect(bustype='socketcan', channel='can0')
	print("network connected")

	print(network.scanner.search(),"search ended")
	time.sleep(0.05)
	nodes = network.scanner.nodes
	for node_id in nodes:
		print("found node with id: ", node_id)
	if nodes.count() == 0:
		return nodes
	else:
		return "No node found"
