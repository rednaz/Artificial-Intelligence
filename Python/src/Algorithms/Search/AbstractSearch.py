# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:51:42 2016

@author: Zander
"""

from Graph import Node, Graph

class AbstractSearch:
    def  __init__(self, graph, queue):
        self.Graph = graph
        self.Queue = queue
        self.SearchTree = Graph()
        self.Visited = list()
        
    def Search(self):
        while (self.Queue.HasNext()):
            next = self.Queue.GetNext()
            newNode = Node(next.Value)
            
            self.SearchTree.AddNode(newNode)
            
            for edge in next.Edges:
                if (self.Visited.Contains(edge)):
                    continue
                
                self.Visited.Add(edge.Node)
                
                self.SearchTree.AddDirectedEdge(newNode, edge.Node)
                
                self.Add(edge)

    def Add(self, edge):
        self.Queue.Add(edge.Node)