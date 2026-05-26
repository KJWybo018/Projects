# Author: Kyle Wybo
# Created: 05/26/2026

class Edge:
  def __init__(self, weight, target_node=None):
    self.weight = weight
    self.to_node = target_node


class Node:
  def __init__(self, data, memMax, currUse):
    self.data = data
    self.edges = []
    self.distance = float('inf')
    self.memMax = memMax
    self.currUse = currUse
