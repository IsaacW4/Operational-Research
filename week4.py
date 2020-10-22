# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy

def isprime(n):
    """ This is the description of the function ~ Loves it
    
    Parameters 
    ----------
    n : int
        int to check if prime
    
    Returns
    -------
    bool
       true if n prime 
       
       """   
    if n>=2:
        for i in range(2,n):
            if not (n % i):
                return False
    else:
        return False
    return True


def isprime1(n):
    """ This is the description of the function 2 ~ Loves it +1
    
    Parameters
    ----------
    n : int
        int to check if prime
        
    Returns
    -------
    bool
       true if n prime
       """
    if n>=2:
        for i in range(2, int(numpy.ceil(numpy.sqrt(n)))):
            if not (n % i):
                return False
    else:
        return False
    return True


def wrong_prime():
    """ This is the description of the function 3 ~ Loves it + 2
    
    Returns
    -------
    p : int
        the p with first not prime q
       """
    for p in range(10,16):
        if isprime(p):
            q = 2**p - 1
            if not isprime(q):
                return p
      
        
def mersenne_prime(n_max):
    """ This is the description of the function 4 ~ Loves it + 3
    
    Parameters
    ----------
    n_max : int 
        for p up to n_max
       
    Returns
    -------
    list 
         list of q 
        """
    primes = []
    for a in range(0,n_max):
        b = 2**a - 1 
        if isprime1(a) and isprime1(b):
            primes.append(b)
    return primes


       
        
        
        
