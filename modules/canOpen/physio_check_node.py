import canopen
import time 
network = canopen.Network()
network.connect(bustype='socketcan', channel='can0')
print("network connected")
network.scanner.search()
print("search ended")
time.sleep(9.05)
for node_id in network.scanner.nodes:
	print("found node with id: ", node_id)
