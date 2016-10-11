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
    print("Building directed graph based on adjacency matrix")
    size = len(adjacencyMatrix)
    nodes = list()
    graph = Graph()
    
    for x in range(size):
        newNode = Node([1, size])
        nodes.append(newNode)
        graph.AddNode(newNode)
        print("Created Page " + str(x))
    
    for x in range(size):
        for y in range(size):
            if adjacencyMatrix[x][y] == 1:
                graph.AddDirectedEdge(nodes[x], nodes[y])
                print("Page " + str(x) + " links to Page " + str(y))
                
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
    
def PageRank(graph, convergence):
    damping = [85, 100]
    
    nodeLength = len(graph.Nodes)
    
    #pageRank = [[1 for x in range(nodeLength)] for y in range(2)]
    
    running = True
    
    while running:        
        newPageRank = [[0 for x in range(2)] for y in range(nodeLength)]
                
        for x in range(nodeLength):            
            newPageRank[x][0] = damping[1] - damping[0]
            newPageRank[x][1] = nodeLength * damping[1]
        
        for x in range(nodeLength):
            for edge in graph.Nodes[x].Edges:
                index = graph.Nodes.index(edge.Node)
                
                #newPageRank[index] = newPageRank[index] + graph.Nodes[x].value/(len(edge.Node.Edges))
                newPageRank[index][0] = ((graph.Nodes[x].Value[1] * len(graph.Nodes[x].Edges)) * newPageRank[index][0] * damping[1]) + (newPageRank[index][1] * graph.Nodes[x].Value[0] * damping[0])
                newPageRank[index][1] = newPageRank[index][1] * (graph.Nodes[x].Value[1] * len(graph.Nodes[x].Edges)) * damping[1]
                
                divisor = gcd(newPageRank[index][0], newPageRank[index][1])
                
                newPageRank[index][0] = newPageRank[index][0] / divisor
                newPageRank[index][1] = newPageRank[index][1] / divisor
               
        running = False               
               
        for x in range(nodeLength):
            newRank = newPageRank[x][0] / newPageRank[x][1]
            oldRank = graph.Nodes[x].Value[0] / graph.Nodes[x].Value[1]
            
            if abs((newRank - oldRank) / ((newRank + oldRank) / 2)) > convergence:
                running = True
                break
                
        for x in range(nodeLength):
            graph.Nodes[x].Value[0] = newPageRank[x][0]
            graph.Nodes[x].Value[1] = newPageRank[x][1]
        
    pageRank = [[0 for x in range(2)] for y in range(nodeLength)]
                
    for x in range(nodeLength):
        pageRank[x][0] = graph.Nodes[x].Value[0]
        pageRank[x][1] = graph.Nodes[x].Value[1]
        #print("pageRank[x][0]: " + str(pageRank[x][0]) + "  [x][1]: " + str(pageRank[x][1]))
        
    return pageRank
    
with open('data.txt') as file:
    pageRankData = [[int(digit) for digit in line.strip()] for line in file]

graph = GraphBuilder(pageRankData)
pageRank = PageRank(graph, .01)

print()
print("Calculated page ranks: ")
count = 0

for rank in pageRank:
    print ("Page " + str(count) + ": " + str((rank[0]) / (rank[1])) + " or " + str(rank[0]) + "/" + str(rank[1]))
    count = count + 1