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
    def  __init__(self, graph, queue, startNode, goalNode):
        self.Graph = graph
        self.Queue = queue
        self.SearchTree = Graph()
        self.Visited = list()
        
        self.StartNode = startNode
        self.GoalNode = goalNode
        self.Queue.Add(self.StartNode)
        self.Visited.append(self.StartNode)
        
    def Search(self):
        while (self.Queue.HasNext()):
            next = self.Queue.GetNext()
            newNode = Node(next.Value)
            
            self.SearchTree.AddNode(newNode)
            
            if (next == self.GoalNode):
                return self.SearchTree
            
            for edge in next.Edges:
                if (edge.Node in self.Visited):
                    continue
                
                self.Visited.append(edge.Node)
                
                self.SearchTree.AddDirectedEdge(newNode, edge.Node)
                
                self.Add(edge)

    def Add(self, edge):
        self.Queue.Add(edge.Node)
        
    def Print(self):
        self.SearchTree.Print()