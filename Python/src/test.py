# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 22:37:10 2016

@author: Zander
"""

from Graph import Graph, Node

graph = Graph()
aNode = Node('A')
bNode = Node('B')

graph.AddNode(aNode)
graph.AddNode(bNode)

graph.AddBiDirectedEdge(aNode, bNode)