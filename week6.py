# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 20:16:27 2018

@author: Isaac
"""

import numpy

def sort_minimum(numbers):
    """ This is the description of the function ~ Loves it1
    
    Parameters
    ----------
    numbers : array
              array to sort
    
    Returns
    -------
    array
        printed array
        
        """
    n = []
    for x in numbers:
        n.append(x)
    n = [float(x) for x in n]
    n.sort()
    return n
    
def bubble_sort(numbers):
    
        """ This is the description of the function ~ Loves it2
    
    Parameters
    ----------
    numbers : array
              array to sort
    
    Returns
    -------
    array
        printed array
        
        """
        n = []
        for x in numbers:
            n.append(x)
        n = [float(x) for x in n]
        n.sort()
        return n

def complex_sort(numbers):
        """ This is the description of the function ~ Loves it3
    
    Parameters
    ----------
    numbers : array
              array to sort
    
    Returns
    -------
    array
        printed array
        
        """
        return sorted(numbers, key=abs)

  
     
        

