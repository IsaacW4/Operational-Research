# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 20:15:57 2018

@author: Isaac
"""

import numpy
import scipy.constants


def cuboid_volume(a,b,c):
    """
    Parameters
    ----------
     a : float 
     b : float
     c : cloat 
     
    Return 
    ------
    cuboid_volume : float
    """
    
    if a < 0 or b < 0 or c < 0:
        return 0 
    else:
        return a*b*c        
     

def triangle_area(a,b,c):
    """ 
    Parameters :
        a : float
        b : float
        c : float
    Return : 
        triangle_area : float 
    """
    
    s = ((a+b+c)/2)
    return numpy.sqrt(s*(s-a)*(s-b)*(s-c))


def fall_time(start_height):
    """
    Parameters : 
        start_height : float
    Return : 
        fall_time : float
    """
    
    if start_height < 0 : 
        return 0
    else:
        return numpy.sqrt((2*start_height) / scipy.constants.g)



#Testing for comments