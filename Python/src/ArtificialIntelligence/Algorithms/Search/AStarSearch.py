# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 18:28:00 2016

@author: Eric
"""

import sys

sys.path.append('C:\Projects\Artificial Intelligence\Python\src\ArtificialIntelligence\Structure\Queues')

from UniformCostSearch import UniformCostSearch
from ZPriorityQueue import ZPriorityQueue

class AStarSearch(UniformCostSearch):
    def __init__(self, graph, startNode, heuristics):
        super().__init__(graph, ZPriorityQueue(), startNode)
        
        self.Heuristics = heuristics
        
    def CalculateWeight(self, edge, weight):
        currentHeuristic = next(heuristic for heuristic in self.Heuristics if heuristic.Node == edge.Node)
        
        return super(AStarSearch, self).CalculateWeight(edge, weight) + currentHeuristic.Value