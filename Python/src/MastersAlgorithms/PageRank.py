# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:26:47 2016

@author: Eric
"""

def PageRank(M, d, quadraticError):
    N = size(M, 2)
    v = rand(N, 1)
    v = v / norm(v, 1)
    lastV = ones(N, 1) * inf
    
    M_hat = (d .* M) + (((1 - d) / N) * ones(N, N))
    
    while(True):
        lastV = v
        v = M_hat * v