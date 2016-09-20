# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:33:51 2016

@author: Eric
"""

""" BFS DFS, UCS """

import sys

sys.path.append('D:\Projects\Artificial Intelligence\Python\src\ArtificialIntelligence\Math\Graph')
sys.path.append('D:\Projects\Artificial Intelligence\Python\src\ArtificialIntelligence\Algorithms\Search')

from Graph import Graph
from Node import Node
from BreadthFirstSearch import BreadthFirstSearch 
from DepthFirstSearch import DepthFirstSearch 

graph = Graph()
aNode = Node('A')
bNode = Node('B')
cNode = Node('C')
dNode = Node('D')

graph.AddNode(aNode)
graph.AddNode(bNode)
graph.AddNode(cNode)
graph.AddNode(dNode)

graph.AddBiDirectedEdge(aNode, bNode)
graph.AddBiDirectedEdge(aNode, cNode)
graph.AddBiDirectedEdge(bNode, dNode)

bfs = BreadthFirstSearch(graph, aNode)

bfs.Search()

graph.Print()
print()
bfs.Print()

print()

dfs = DepthFirstSearch(graph, aNode)

dfs.Search()
dfs.Print()

print('Stop')