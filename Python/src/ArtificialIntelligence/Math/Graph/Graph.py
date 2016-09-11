# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 22:42:29 2016

@author: Zander
"""

from Edge import Edge

class Graph:
    def __init__(self):
        self.Nodes = set()

    def AddNode(self, node):
        self.Nodes.add(node)

    def AddDirectedEdge(self, startNode, endNode):
        startNode.Edges.add(Edge(endNode))

    def AddBiDirectedEdge(self, startNode, endNode):
        self.AddDirectedEdge(startNode, endNode)
        self.AddDirectedEdge(endNode, startNode)