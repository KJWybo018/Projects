# Author: Kyle Wybo
# Date Created: 05/28/2026

class Event():

  def __init__(self, priority, event_type, packetData, nodeData):
    self.priority = priority
    self.event_type = event_type
    self.packetData = packetData
    self.nodeData = nodeData

class Packet():

  def __init__(self, start, end, packID, size):
    self.start = start
    self.end = end
    self.packID = packID
    self.size = size


