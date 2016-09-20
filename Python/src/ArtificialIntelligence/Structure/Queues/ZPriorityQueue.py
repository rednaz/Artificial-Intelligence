# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:28:11 2016

@author: Zander
"""

from heapq import heapq
from IQueue import IQueue

class ZPriorityQueue(IQueue):
    def __init__(self):
        self.ZPQ = heapq()
    
    def HasNext(self):
        return not self.ZPQ.empty()
    
    def GetNext(self):
        return self.ZPQ.heappop()
    
    def Add(self, item):
        self.ZPQ.heappush(item, 1)
        
    def Add(self, item, priority):
        if item in self.ZPQ.heap:
            self.ZPQ.remove(item)
        
        self.ZPQ.heappush(item, priority)