# Author: Kyle Wybo
# Created: 05/26/2026

import heapq

def djikstra(graph, start):
  distances = {node: float('inf') for node in graph}
  distances[start] = 0

  predecessors = {node: None for node in graph}

  priority_queue = [(0, start)]

  while priority_queue:
    current_distance, current_node = heapq.heappop(priority_queue)

    if current_distance > distances[current_node]:
      continue

    for neighbor, weight in graph[current_node].items():
      distance = current_distance + weight

      if distance < distances[neighbor]:
        distances[neighbor] = distance
        predecessors[neighbor] = current_node
        heapq.heappush(priority_queue, (distance, neighbor))

  return distances, predecessors


