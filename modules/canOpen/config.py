import canopen

def connect_node(id, bustype='socketcan', channel='can0'):
    '''
    Returns network and node as a tuple.
    '''
    # Start with creating a network representing one CAN bus
    network = canopen.Network()

    # Add some nodes with corresponding Object Dictionaries
    node = canopen.RemoteNode(id, 'ASDA_A2_1042sub980_C.eds')
    network.add_node(node)
    network.connect(bustype=bustype, channel=channel)
    return network, node

def init_drive(node, interval):
    node.nmt.state = 'PRE-OPERATIONAL'

    node.sdo['Controlword'].raw=128 # Clear_Error
    node.sdo['Controlword'].raw=0   # Switch_ON
    node.sdo['Controlword'].raw=6   #
    node.sdo['Controlword'].raw=7   # Init & Run
    node.sdo['Controlword'].raw=15  #

    # Set speed limit in rpm : 25 -> 1 
    node.sdo['P1-55'].raw = 25 * 10

    # Read PDO configuration from node
    node.rpdo.read()
    node.tpdo.read()

    # Re-map TPDO[1]
    node.tpdo[1].clear()
    node.tpdo[1].add_variable('Position actual value')
    node.tpdo[1].add_variable('Velocity actual value')
    node.tpdo[1].enabled = True
    
    # Re-map TPDO[2]
    node.tpdo[2].clear()
    node.tpdo[2].add_variable('Torque actual value')
    node.tpdo[2].enabled = True
    
    # Save new PDO configuration to node
    node.tpdo.save()
    
    # Re-map RPDO[1]
    node.rpdo[1].clear()
    node.rpdo[1].add_variable('Target Position')
    node.rpdo[1].add_variable('Profile velocity')
    node.rpdo[1].enabled = True

    # Re-map RPDO[2]
    node.rpdo[2].clear()
    node.rpdo[2].add_variable('Target velocity')
    node.rpdo[2].add_variable('Target torque')
    node.rpdo[2].enabled = True
    
    # Save new PDO configuration to node
    node.rpdo.save()
    
    # Start PDO transmission with specific interval
    node.rpdo[1].start(interval)
    node.rpdo[2].start(interval)

def setModesOfOperation(node, mode):
    node.sdo['Modes of operation'].raw = mode

def start(self, node, interval):
    self.init_drive(node, interval)
    print("node ", node, " initiated.")
    node.nmt.state = 'OPERATIONAL'
    print("node ", node, " is operational.")

def stop(node):
    setTargetVelocity(node,0)
    setTargetTorque(node,0)
    node.sdo['Controlword'].raw = 0
    
def disconnect_network(network):    
    network.disconnect()
    print("network ", network, " disconnected.")

def setTargetPosition(node, tarPos):
    node.rpdo[1]['Target position'].raw = tarPos

def setProfileVelocity(node, profVel):
    node.rpdo[1]['Profile velocity'].raw = profVel

def setTargetVelocity(node, tarVel):
    node.rpdo[2]['Target velocity'].raw = tarVel

def setTargetTorque(node, tarTor):
    node.rpdo[2]['Target torque'].raw = tarTor

def getPosition(node):
    return node.tpdo[1]['Position actual value'].raw

def getVelocity(node):
    return node.tpdo[1]['Velocity actual value'].raw

def getTorque(node):
    return node.tpdo[2]['Torque actual value'].raw
