#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:57:25 2021

@author: cgarate
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''

    if exp == 0:
        return 1
    else:
        base = base * recurPower(base, exp - 1)
        print(base)
        
    return base
    
recurPower(0.15, 6)
    