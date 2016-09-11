# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:33:51 2016

@author: Eric
"""

""" BFS DFS, UCS """

import sys

sys.path.append('C:\Projects\ArtificialIntelligence\Python\src\ArtificialIntelligence\Math\Graph')
sys.path.append('C:\Projects\ArtificialIntelligence\Python\src\ArtificialIntelligence\Algorithms\Search')

from Graph import Graph
from Node import Node
from BreadthFirstSearch import BreadthFirstSearch 

graph = Graph()
aNode = Node('A')
bNode = Node('B')

graph.AddNode(aNode)
graph.AddNode(bNode)

graph.AddBiDirectedEdge(aNode, bNode)

bfs = BreadthFirstSearch(graph)

bfs.Search()
bfs.Print()

print('Stop')