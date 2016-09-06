# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:16:42 2016

@author: Zander
"""

from queue import Queue
import IQueue

class ZQueue(metaclass=IQueue):
    def __init__(self):
        self.ZQ = Queue()
    
    def HasNext(self):
        return not self.ZQ.empty()
    
    def GetNext(self):
        return self.ZQ.get()
    
    def Add(self, item):
        self.ZQ.put(item)