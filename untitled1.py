# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 11:07:22 2018

@author: Isaac
"""

import numpy

c = [1,2,3]
numpy.array(c)

a = numpy.matrix("1 2; 2 6")
b = numpy.matrix("1 2 ; 4 5 ")
print(a)
print(b)
print(a-b)
numpy.linalg.matrix_rank(b)

g = numpy.matrix("1 2 3 ; 4 5 6 ; 7 8 9")
print(g)
numpy.linalg.det(g)

k = numpy.matrix("1 2 ; 3 4")
numpy.linalg.det(k)

v = numpy.array([[1,2], [3,4]])
print(v)
numpy.linalg.det(v)