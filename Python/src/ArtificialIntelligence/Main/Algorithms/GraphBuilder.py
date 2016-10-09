# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:34:52 2016

@author: Zander
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
        newNode = Node([1, size])
        nodes.append(newNode)
        graph.AddNode(newNode)
    
    for x in range(size):
        for y in range(size):
            if adjacencyMatrix[x][y] == 1:
                graph.AddDirectedEdge(nodes[x], nodes[y])
                
    #graph.Print()
    
    return graph
    
def gcd(m, n):
	if (m <=0 or n <= 0):
		return null
	a=0
	x=1
	b=1
	y=0
	c=m
	d=n
	r=1

	while (r > 0):
		q = int(c / d)
		r = (c % d)

		if (r == 0):
			break
	
		c=d
		d=r
		t=x
		x=a
		a=(t - ( q * a ))
		t=y
		y=b
		b=(t-(q*b))
	return (d)
    
def PageRank(graph, iterations):
    damping = 1
    
    nodeLength = len(graph.Nodes)
    
    #pageRank = [[1 for x in range(nodeLength)] for y in range(2)]
    
    while iterations > 0:        
        newPageRank = [[0 for x in range(2)] for y in range(nodeLength)]
        
        #for x in nodeLength:
        #    if len(graph.Nodes[x].Edges) == 0:
        #        dp = dp + (damping * (pageRank[x][0] / pageRank[x][0]) / nodeLength)
                
        for x in range(nodeLength):            
            newPageRank[x][0] = 1 - damping
            newPageRank[x][1] = nodeLength
        
        for x in range(nodeLength):
            for edge in graph.Nodes[x].Edges:
                index = graph.Nodes.index(edge.Node)
                
                #newPageRank[index] = newPageRank[index] + graph.Nodes[x].value/(len(edge.Node.Edges))
                newPageRank[index][0] = ((graph.Nodes[x].Value[1] * len(graph.Nodes[x].Edges)) * newPageRank[index][0]) + (newPageRank[index][1] * graph.Nodes[x].Value[0])
                newPageRank[index][1] = newPageRank[index][1] * (graph.Nodes[x].Value[1] * len(graph.Nodes[x].Edges))
                
                divisor = gcd(newPageRank[index][0], newPageRank[index][1])
                
                newPageRank[index][0] = newPageRank[index][0] / divisor
                newPageRank[index][1] = newPageRank[index][1] / divisor
                
        for x in range(nodeLength):
            graph.Nodes[x].Value[0] = newPageRank[x][0]
            graph.Nodes[x].Value[1] = newPageRank[x][1]
            
        iterations = iterations - 1
        
    pageRank = [[0 for x in range(2)] for y in range(nodeLength)]
                
    for x in range(nodeLength):
        pageRank[x][0] = graph.Nodes[x].Value[0]
        pageRank[x][1] = graph.Nodes[x].Value[1]
        
    return pageRank
    
matrix = [[0 for x in range(6)] for y in range(6)]

"""
010000
001111
000001
000010
001000
100000
"""

matrix[0][1] = 1
matrix[1][2] = 1
matrix[1][3] = 1
matrix[1][4] = 1
matrix[1][5] = 1
matrix[2][5] = 1
matrix[3][4] = 1
matrix[4][2] = 1
matrix[5][0] = 1

graph = GraphBuilder(matrix)
pageRank = PageRank(graph, 17)

print()

for rank in pageRank:
    print (rank[0] / rank[1])