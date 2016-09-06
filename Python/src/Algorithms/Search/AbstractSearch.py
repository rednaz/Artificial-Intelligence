# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 15:51:42 2016

@author: Zander
"""

class AbstractSearch:
    def  __init__(self, graph, queue):
        self.Graph = graph
        self.Queue = queue