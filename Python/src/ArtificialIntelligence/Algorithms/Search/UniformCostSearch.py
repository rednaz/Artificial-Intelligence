# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:17:45 2016

@author: Zander
"""

import sys

sys.path.append('D:\Projects\Artificial Intelligence\Python\src\ArtificialIntelligence\Structure\Queues')

from AbstractSearch import AbstractSearch
from ZPriorityQueue import ZPriorityQueue

class UniformCostSearch(AbstractSearch):
    def __init__(self, graph, startNode, goalNode):
        super().__init__(graph, ZPriorityQueue(), startNode, goalNode)

        self.Weights = list()
        
        for item in graph.Nodes:
            self.Weights.insert(WeightedItem(item, sys.maxint))
            
        next(weightedItem for weightedItem in self.Weights if weightedItem.Item == startNode).Weight = 0
        
    def Add(self, edge):
        if (self.SearchTree.Nodes.count == 0):
            prevWeight = 0
        else:
            prevNode = next(node for node in self.SearchTree if edge in node.Edges)
            prevWeight = next(weightedItem for weightedItem in self.Weights if weightedItem.Item == prevNode).Weight
            
        newWeight = edge.Weight + prevWeight
            
        self.Queue.Add(edge.Node, newWeight)
        
        next(weightedItem for weightedItem in self.Weights if weightedItem.Item == edge.Node).Weight = newWeight
        
class WeightedItem:
    def __init__(self, item, weight):
        self.Item = item
        self.Weight = weight