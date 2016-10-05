# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:44:12 2016

@author: Eric
"""

class GeneticSearch():
    def __init__(self, population, fitnessFunction):
        self.Population = population
        self.FitnessFunction = fitnessFunction
    
    def Search(self):
        while(True):
            parents = list()
            children = list()
            for individual in self.Population:
                parents.append((individual, fitnessFunction(individual)))
                
            for i in range(population.count):
                x = 