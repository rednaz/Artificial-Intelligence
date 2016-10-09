# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:34:52 2016

@author: Zander, James, Mason
"""
    
class Node:
    def __init__(self, value):
        self.Value = value
        self.Edges = list()

class Edge:
    def __init__(self, node, weight=1):
        self.Node = node
        self.Weight = weight

class Graph:
    def __init__(self):
        self.Nodes = list()

    def AddNode(self, node):
        self.Nodes.append(node)

    def AddDirectedEdge(self, startNode, endNode, weight = 1):
        startNode.Edges.append(Edge(endNode, weight))

    def AddBiDirectedEdge(self, startNode, endNode, weight = 1):
        self.AddDirectedEdge(startNode, endNode, weight)
        self.AddDirectedEdge(endNode, startNode, weight)
        
    def Print(self):
        for node in self.Nodes:
            for edge in node.Edges:
                nodeValue = node.Value
                edgeNodeValue = edge.Node.Value
                print(str(nodeValue) + '->' + str(edgeNodeValue))

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
    
with open('data.txt') as file:
    pageRankData = [[int(digit) for digit in line.strip()] for line in file]

graph = GraphBuilder(pageRankData)
pageRank = PageRank(graph, 100)

print()

for rank in pageRank:
    print (rank[0] / rank[1])