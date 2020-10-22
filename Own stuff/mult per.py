# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:08:02 2019

@author: Isaac
"""

def per(n):
    if len(str(n)) == 1:
        print (n)
        return "Done"
    
    digits = [int(i) for i in str(n)]
    
    result = 1
    for j in digits:
        result *= j 
    print(result)
    per(result)