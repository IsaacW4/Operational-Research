# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:11:49 2019

@author: Isaac
"""

def muldiv(n):
    digits = [int(i) for i in str(n)]
    mul = 1
    for j in digits: 
        mul *= j
        
    result = (int(int(n) / (mul)))
    print(result)
    
def prime(n):
    return all(n % j for j in range(2, n))
        