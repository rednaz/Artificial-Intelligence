# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:05:43 2016

@author: Zander
"""

from abc import ABCMeta, abstractmethod

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