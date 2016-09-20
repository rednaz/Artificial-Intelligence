# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 11:44:56 2016

@author: Eric
"""

import sys

sys.path.append('C:\Projects\ArtificialIntelligence\Python\src\ArtificialIntelligence\Structure\Queues')

from AbstractSearch import AbstractSearch
from ZStack import ZStack

class DepthFirstSearch(AbstractSearch):
    def __init__(self, graph, startNode):
        super().__init__(graph, ZStack(), startNode)