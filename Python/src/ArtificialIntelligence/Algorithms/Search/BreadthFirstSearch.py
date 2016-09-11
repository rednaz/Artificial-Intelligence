# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:12:38 2016

@author: Zander
"""

import sys

sys.path.append('C:\Projects\ArtificialIntelligence\Python\src\ArtificialIntelligence\Structure\Queues')

from AbstractSearch import AbstractSearch
from ZQueue import ZQueue

class BreadthFirstSearch(AbstractSearch):
    def __init__(self, graph):
        super().__init__(graph, ZQueue())