# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:42:42 2016

@author: Eric
"""

class HillClimbingSearch():
    def __init__(self, nextStatesFunction, evalFunction):
        self.NextStatesFunction = nextStatesFunction
        self.EvalFunction = evalFunction

    def Search(self, startState):
        currentState = startState
        nextEval = (2^63)-1
        
        while True:
            for state in self.NextStatesFunction(currentState):          
                stateEval = self.EvalFunction(state)
                
                if stateEval < nextEval:           
                    nextState = state
                    nextEval = stateEval
                    
            if nextEval >= self.EvalFunction(currentState):
                return currentState
            
            currentState = nextState