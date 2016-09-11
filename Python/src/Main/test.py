# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:33:51 2016

@author: Eric
"""



from Math.Graph import Graph, Node

graph = Graph()
aNode = Node('A')
bNode = Node('B')

graph.AddNode(aNode)
graph.AddNode(bNode)

graph.AddBiDirectedEdge(aNode, bNode)