# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 20:15:11 2016

@author: Eric
"""

import sys

sys.path.append('D:\Projects\Artificial Intelligence\Python\src\ArtificialIntelligence\Math\Graph')
sys.path.append('D:\Projects\Artificial Intelligence\Python\src\ArtificialIntelligence\Algorithms\Search')

from Graph import Graph
from Node import Node
from BreadthFirstSearch import BreadthFirstSearch 
from DepthFirstSearch import DepthFirstSearch 
from UniformCostSearch import UniformCostSearch 

graph = Graph()
sNode = Node('S')
aNode = Node('A')
bNode = Node('B')
cNode = Node('C')
dNode = Node('D')
eNode = Node('E')
fNode = Node('F')
gNode = Node('G')

graph.AddNode(sNode)
graph.AddNode(aNode)
graph.AddNode(bNode)
graph.AddNode(cNode)
graph.AddNode(dNode)
graph.AddNode(eNode)
graph.AddNode(fNode)
graph.AddNode(gNode)

graph.AddBiDirectedEdge(sNode, aNode, 5)
graph.AddBiDirectedEdge(sNode, dNode, 4)
graph.AddBiDirectedEdge(aNode, bNode, 3)
graph.AddBiDirectedEdge(aNode, dNode, 8)
graph.AddBiDirectedEdge(bNode, cNode, 1)
graph.AddBiDirectedEdge(bNode, eNode, 2)
graph.AddBiDirectedEdge(dNode, eNode, 7)
graph.AddBiDirectedEdge(eNode, fNode, 6)
graph.AddBiDirectedEdge(fNode, gNode, 9)


print("BFS")
BreadthFirstSearch(graph, sNode).Search(gNode).Print()

print("DFS")
DepthFirstSearch(graph, sNode).Search(gNode).Print()

print("UCS")
UniformCostSearch(graph, sNode).Search(gNode).Print()