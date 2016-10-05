# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:59:34 2016

@author: Eric
"""

import sys

sys.path.append('C:\Projects\ArtificialIntelligence\Python\src\ArtificialIntelligence\Math\Graph')
sys.path.append('C:\Projects\ArtificialIntelligence\Python\src\ArtificialIntelligence\Algorithms\Search')

from HillClimbingSearch import HillClimbingSearch
import random
import copy

def ChessHeuristic(board):
    count = 0
    
    for x in range(problemSize):
        for y in range(x + 1, problemSize):
            if (board[x] == board[y]):
                count = count + 1
            elif (board[x] + x == board[y] + y):
                count = count + 1
            elif (board[x] + x + (y-x) * 2 == board[y] + y):
                count = count + 1
    
    return count
        
def NextStates(board):
    states = list()
    
    for i in range(problemSize):
        for j in range(problemSize):
            newState = copy.deepcopy(chessBoard)
            newState[i] = j
            states.append(newState)
    
    return states

problemSize = 8
    
hillClimbing = HillClimbingSearch(NextStates, ChessHeuristic)

while(True):
    chessBoard = [random.randint(0, problemSize-1) for x in range(problemSize)]
    
    print (chessBoard)
    
    lastState = hillClimbing.Search(chessBoard)
    lastHeuristic = ChessHeuristic(lastState)
    
    print ("State: " + str(lastState))
    print ("Heuristic: " + str(lastHeuristic))
    
    if (lastHeuristic == 0):
        break