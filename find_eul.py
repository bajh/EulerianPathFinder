class TourFinder:

  def __init__(self, graph):
    self.graph = graph

  def find_tour(self):
    return Node(self.graph[0][0], self.graph[0][0], None, self.graph).find_next

class Node:

  def __init__(self, name, origin, traveled, untraveled):
    self.name = name
    self.origin = origin
    self.traveled = traveled
    self.attempted = []
    self.untraveled = untraveled

  def complete_tour(self):
    len(untraveled) == 0 

  def neighbors(self):
    edges = []
    for edge in self.untraveled:
      if (self.origin == self.name):
        if (self.name in edge):
          edges.append(edge)
      else:
        if (self.name in edge) and (self.origin not in edge):
          edges.append(edge)
    return edges

  def find_next(self):
    if complete_tour:
      return traveled
    elif len(neighbors) == 0:
      return None
    else:
      for neighbor in neighbors:
        next_node = [node for node in neighbor if (self.name != node)][0]
        next = Node(next_node, self.origin, self.traveled + neighbor, [edge for edge in untraveled if edge != neighbor]).find_next
        if next:
          return next


my_graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]

print TourFinder(my_graph).find_tour()
