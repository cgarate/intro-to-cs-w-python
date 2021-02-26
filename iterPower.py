#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:50:03 2021

@author: cgarate
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1.0
    
    result = base
    while exp > 1:
        exp -= 1
        result = result * base
        print(result)
        
        
    print(result)
    return result

iterPower(-8.45, 6)