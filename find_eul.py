class TourFinder:

  def __init__(self, graph):
    self.graph = graph

  def find_tour(self):
    return Node(self.graph[0][0], self.graph[0][0], [], self.graph).find_next()

class Node:

  def __init__(self, name, origin, traveled, untraveled):
    self.name = name
    self.origin = origin
    self.traveled = traveled
    self.attempted = []
    self.untraveled = untraveled

  def complete_tour(self):
    if len(self.untraveled) == 1:
      if len(self.neighbors()):
        if self.origin in self.neighbors()[0]:
          return True

  def remaining_origin_nodes(self):
    return [edge for edge in self.untraveled if self.origin in edge]

  def neighbors(self):
    edges = []
    for edge in self.untraveled:
      if (self.origin == self.name):
        if (self.name in edge):
          edges.append(edge)
      elif ((self.origin in edge) and len(self.untraveled) == 1):
        edges.append(edge)
      else:
        # This doesn't allow it to loop around!!
        if (self.name in edge) and ((self.origin not in edge) or (self.remaining_origin_nodes() > 2)):
          edges.append(edge)
    return edges

  def find_next(self):
    if self.complete_tour():
      self.traveled += [self.neighbors()[0]]
      return self.traveled
    elif len(self.neighbors()) == 0:
      return None
    else:
      for neighbor in self.neighbors():
        next_node = [node for node in neighbor if (self.name != node)][0]
        next = Node(next_node, self.origin, list(self.traveled + [neighbor]), [edge for edge in self.untraveled if edge != neighbor]).find_next()
        if next:
          return next

# Test example:
# my_graph = [(8, 16), (8, 18), (16, 17), (18, 19),
# (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
# (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
# (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]

# print TourFinder(my_graph).find_tour()