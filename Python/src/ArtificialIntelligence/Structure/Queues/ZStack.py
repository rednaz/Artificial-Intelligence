# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 11:45:53 2016

@author: Eric
"""

from IQueue import IQueue

class ZStack(IQueue):
    def __init__(self):
        self.ZS = list()
    
    def HasNext(self):
        return len(self.ZS) > 0
    
    def GetNext(self):
        return self.ZS.pop()
    
    def Add(self, item):
        self.ZS.append(item)