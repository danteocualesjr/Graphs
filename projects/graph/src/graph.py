#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    """ Vertices always have a label and a set of edges. """
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)

class Graph:    
    """ Represent a graph as a dictionary of vertices mapping labels to edges. """
    """ Type of graph: adjacency list """
    def __init__(self):
        self.vertices = {}

    def add_edge(self, start, end, bidirectional=True):
        """ Adding an edge from start to end. """
        if start not in self.vertices or end not in self.vertices:
            raise Exception("%s or %s does not exist" %(start, end))
        else:
            self.vertices[start].add(end)
            if bidirectional == True:
                self.vertices[end].add(start)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            raise ValueError("That vertex already exists in the graph.")

# Testing Graph implementation:

graph = Graph() # Instantiating an empty graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)