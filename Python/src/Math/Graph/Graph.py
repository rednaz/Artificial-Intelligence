# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 22:42:29 2016

@author: Zander
"""

import Edge

class Graph:
    def __init__(self):
        self.Nodes = list()

    def AddNode(self, node):
        self.Nodes.Add(node)

    def AddDirected(self, startNode, endNode):
        startNode.Edges.Add(Edge(endNode))

    def AddBiDirectedEdge(self, startNode, endNode):
        self.AddDirectedNode(startNode, endNode)
        self.AddDirectedNode(endNode, startNode)