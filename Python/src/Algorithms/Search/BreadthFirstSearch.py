# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:12:38 2016

@author: Zander
"""

import AbstractSearch
from Queues import ZQueue

class BreadthFirstSearch(AbstractSearch):
    def __init__(self, graph):
        AbstractSearch(graph, ZQueue)