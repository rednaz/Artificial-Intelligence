# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:28:11 2016

@author: Zander
"""

import heapq
import itertools
from IQueue import IQueue

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