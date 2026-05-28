# Author: Kyle Wybo
# Date Created: 05/28/2026

import heapq

class EngineEvent():

  def __init__(self):
    self.queue = []


  def add_event(self, priority, event):
    heapq.heappush(self.queue, (priority, event))


  def run(self):

    while (self.queue):
      priority, event = heapq.heappop(self.queue)
      if (event.event_type == "packet_arrived_router"):
        pass
      elif (event.event_type == "packet_leaves_router"):
        pass
      elif (event.event_type == "packet_arrive_dest"):
        pass

    
