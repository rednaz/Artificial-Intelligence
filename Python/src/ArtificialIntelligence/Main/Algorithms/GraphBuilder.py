# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:34:52 2016

@author: Zander
"""

"""
010000
001110
000001
001010
000001
100000
"""

import sys

sys.path.append('D:\Projects\Artificial Intelligence\Python\src\ArtificialIntelligence\Math\Graph')

from Graph import Graph
from Node import Node

def GraphBuilder(adjacencyMatrix):
    size = len(adjacencyMatrix)
    nodes = list()
    graph = Graph()
    
    for x in range(size):
        newNode = Node(x)
        nodes.append(newNode)
        graph.AddNode(newNode)
    
    for x in range(size):
        for y in range(size):
            if adjacencyMatrix[x][y] == 1:
                graph.AddDirectedEdge(nodes[x], nodes[y])

    graph.Print()
    
matrix = [[0 for x in range(6)] for y in range(6)]

matrix[0][1] = 1
matrix[1][2] = 1
matrix[1][3] = 1
matrix[1][4] = 1
matrix[2][5] = 1
matrix[3][2] = 1
matrix[3][4] = 1
matrix[4][5] = 1
matrix[5][0] = 1

GraphBuilder(matrix)