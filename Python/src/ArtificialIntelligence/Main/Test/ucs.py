# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:18:30 2016

@author: Eric
"""

from abc import ABCMeta, abstractmethod
import heapq
import itertools

class IQueue(metaclass=ABCMeta):
    @abstractmethod    
    def HasNext(self):
        pass
    
    @abstractmethod
    def GetNext(self):
        pass
    
    @abstractmethod
    def Add(self, item):
        pass

class AbstractSearch:
    def  __init__(self, graph, queue, startNode):
        self.Graph = graph
        self.Queue = queue
        self.SearchTree = Graph()
        self.Visited = list()
        
        self.StartNode = startNode
        self.Queue.Add(self.StartNode)
        self.Visited.append(self.StartNode)
        
    def Search(self, goalNode):
        while (self.Queue.HasNext()):
            next = self.Queue.GetNext()
            newNode = Node(next.Value)
            
            self.SearchTree.AddNode(newNode)
            
            if (next == goalNode):
                return self.SearchTree
            
            for edge in next.Edges:
                if (edge.Node in self.Visited):
                    continue
                
                self.Visited.append(edge.Node)
                
                self.SearchTree.AddDirectedEdge(newNode, edge.Node)
                
                self.Add(edge)

    def Add(self, edge):
        self.Queue.Add(edge.Node)
        
    def Print(self):
        self.SearchTree.Print()

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
              
        newWeight = edge.Weight + prevWeight
            
        self.Queue._Add_(edge.Node, newWeight)
        
        next(weightedItem for weightedItem in self.Weights if weightedItem.Item == edge.Node).Weight = newWeight
        
class WeightedItem:
    def __init__(self, item, weight):
        self.Item = item
        self.Weight = weight

class ZPriorityQueue(IQueue):
    def __init__(self):
        self.heap = []
        self.values = {}
        self.REMOVED = '<removed-task>'
        self.counter = itertools.count()
    
    def HasNext(self):
        return len(self.heap) > 0
    
    def GetNext(self):
        heapq.heapify(self.heap)
        while self.heap:
            priority, count, item = heapq.heappop(self.heap)
            if item is not self.REMOVED:
                del self.values[item]
                return item
    
    def Add(self, item):
        self._Add_(item, 1)
        
    def _Add_(self, item, priority):
        if item in self.values:
            entry = self.entry_finder.pop(item)
            entry[-1] = self.REMOVED
        
        count = next(self.counter)
        entry = [priority, count, item]
        self.values[item] = entry
        heapq.heappush(self.heap, entry)









class Edge:
    def __init__(self, node, weight):
        self.Node = node
        self.Weight = weight

class Node:
    def __init__(self, value):
        self.Value = value
        self.Edges = set()

class Graph:
    def __init__(self):
        self.Nodes = set()

    def AddNode(self, node):
        self.Nodes.add(node)

    def AddDirectedEdge(self, startNode, endNode, weight = 1):
        startNode.Edges.add(Edge(endNode, weight))

    def AddBiDirectedEdge(self, startNode, endNode, weight = 1):
        self.AddDirectedEdge(startNode, endNode, weight)
        self.AddDirectedEdge(endNode, startNode, weight)
        
    def Print(self):
        for node in self.Nodes:
            for edge in node.Edges:
                print(node.Value + '->' + edge.Node.Value)

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

graph.AddBiDirectedEdge(aNode, bNode, 7)
graph.AddBiDirectedEdge(aNode, cNode, 14)
graph.AddBiDirectedEdge(aNode, dNode, 9)
graph.AddBiDirectedEdge(bNode, dNode, 10)
graph.AddBiDirectedEdge(bNode, eNode, 4)
graph.AddBiDirectedEdge(cNode, dNode, 2)
graph.AddBiDirectedEdge(cNode, fNode, 9)
graph.AddBiDirectedEdge(dNode, eNode, 11)
graph.AddBiDirectedEdge(eNode, fNode, 6)

ucs = UniformCostSearch(graph, aNode)

ucs.Search(fNode).Print()