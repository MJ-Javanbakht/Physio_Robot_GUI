# import psutil, os
# param = os.sched_param(os.sched_get_priority_max(os.SCHED_FIFO))
# print(param)
# os.sched_setscheduler(0, os.SCHED_FIFO, param)
# p = psutil.Process(os.getpid())
# p.nice(-100)
# p.pid = -100
# p.nice()
# p.nice(79)  # set
# p.nice()

class Velocity:

  def init_drive(self, node):
    node.nmt.state = 'PRE-OPERATIONAL'

    node.sdo['Modes of operation'].raw=3 #Velocity Mode

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
    node.tpdo[1].add_variable('Velocity actual value')
    node.tpdo[1].enabled = True
    # Save new PDO configuration to node
    node.tpdo[1].save()

    node.rpdo[1].clear()
    node.rpdo[1].add_variable('Target velocity')
    node.rpdo[1].enabled = True
    node.rpdo.save()
    node.rpdo[1].start(0.005)

  def start(self, node):
    self.init_drive(node)
    print("node ", node, " initiated.")
    node.nmt.state = 'OPERATIONAL'
    print("node ", node, " is operational.")

  def stop(self, node, network):
    node.rpdo[1]['Target velocity'].raw = 0
    node.sdo['Controlword'].raw = 0
    network.disconnect()
    print("network ", network, " disconnected.")

  def setVelocity(self, node, vel):
    node.rpdo[1]['Target velocity'].raw = vel

  def getVelocity(self, node):
    return node.tpdo[1]['Velocity actual value'].raw

  def getPosition(self, node):
    return node.tpdo[1]['Position actual value'].raw