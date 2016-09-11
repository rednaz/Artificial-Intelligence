# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:51:42 2016

@author: Zander
"""

import sys

sys.path.append('C:\Projects\ArtificialIntelligence\Python\src\ArtificialIntelligence\Math\Graph')

from Graph import Graph
from Node import Node

class AbstractSearch:
    def  __init__(self, graph, queue):
        self.Graph = graph
        self.Queue = queue
        self.SearchTree = Graph()
        self.Visited = list()
        
        self.Queue.Add(next(iter(self.Graph.Nodes)))
        
    def Search(self):
        while (self.Queue.HasNext()):
            next = self.Queue.GetNext()
            newNode = Node(next.Value)
            
            self.SearchTree.AddNode(newNode)
            
            for edge in next.Edges:
                if (edge.Node in self.Visited):
                    continue
                
                self.Visited.append(edge.Node)
                
                self.SearchTree.AddDirectedEdge(newNode, edge.Node)
                
                self.Add(edge)

    def Add(self, edge):
        self.Queue.Add(edge.Node)
        
    def Print(self):
        for node in self.SearchTree.Nodes:
            print(node.Value)