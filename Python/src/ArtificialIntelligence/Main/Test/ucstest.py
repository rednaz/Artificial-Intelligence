# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:48:02 2016

@author: Zander
"""

import sys

sys.path.append('D:\Projects\Artificial Intelligence\Python\src\ArtificialIntelligence\Math\Graph')
sys.path.append('D:\Projects\Artificial Intelligence\Python\src\ArtificialIntelligence\Algorithms\Search')

from Graph import Graph
from Node import Node
from UniformCostSearch import UniformCostSearch 

graph = Graph()
aNode = Node('A')
bNode = Node('B')
cNode = Node('C')
dNode = Node('D')
eNode = Node('E')
fNode = Node('F')

graph.AddNode(aNode)
graph.AddNode(bNode)
graph.AddNode(cNode)
graph.AddNode(dNode)
graph.AddNode(eNode)
graph.AddNode(fNode)

graph.AddBiDirectedEdge(aNode, bNode)
graph.AddBiDirectedEdge(aNode, cNode)
graph.AddBiDirectedEdge(aNode, dNode)
graph.AddBiDirectedEdge(bNode, dNode)
graph.AddBiDirectedEdge(bNode, eNode)
graph.AddBiDirectedEdge(cNode, dNode)
graph.AddBiDirectedEdge(cNode, fNode)
graph.AddBiDirectedEdge(dNode, eNode)
graph.AddBiDirectedEdge(eNode, fNode)

ucs = UniformCostSearch(graph, aNode)

ucs.Search(fNode).Print()