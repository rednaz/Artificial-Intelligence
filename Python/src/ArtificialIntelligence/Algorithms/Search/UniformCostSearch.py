# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:17:45 2016

@author: Zander
"""

import sys

sys.path.append('C:\Projects\Artificial Intelligence\Python\src\ArtificialIntelligence\Structure\Queues')

from AbstractSearch import AbstractSearch
from ZPriorityQueue import ZPriorityQueue

class UniformCostSearch(AbstractSearch):
    def __init__(self, graph, startNode):
        super().__init__(graph, ZPriorityQueue(), startNode)

        self.Weights = list()
        
        for item in graph.Nodes:
            self.Weights.append(WeightedItem(item, (2^63-1)))
            
        next(weightedItem for weightedItem in self.Weights if weightedItem.Item == startNode).Weight = 0
        
    def Add(self, edge):
        if (len(self.SearchTree.Nodes) == 0):
            prevWeight = 0
        else:
            for node in self.Graph.Nodes:
                if edge in node.Edges:
                    prevNode = node
                    break
            for weightedItem in self.Weights:
                if weightedItem.Item == prevNode:
                    prevWeight = weightedItem.Weight
                    break
              
        newWeight = self.CalculateWeight(edge, prevWeight)
            
        self.Queue._Add_(edge.Node, newWeight)
        
        next(weightedItem for weightedItem in self.Weights if weightedItem.Item == edge.Node).Weight = newWeight
        
    def CalculateWeight(self, edge, weight):
        return edge.Weight + weight
        
class WeightedItem:
    def __init__(self, item, weight):
        self.Item = item
        self.Weight = weight