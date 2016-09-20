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

    def AddDirectedEdge(self, startNode, endNode, weight = 1):
        startNode.Edges.add(Edge(endNode, weight))

    def AddBiDirectedEdge(self, startNode, endNode, weight = 1):
        self.AddDirectedEdge(startNode, endNode, weight)
        self.AddDirectedEdge(endNode, startNode, weight)
        
    def Print(self):
        for node in self.Nodes:
            for edge in node.Edges:
                print(node.Value + '->' + edge.Node.Value)