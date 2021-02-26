#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:20:45 2021

@author: cgarate
"""
s= "azcbobobegghakl"
numOfVowels = 0
for letter in s:
    if letter in ["a","e","i","o","u"]:
        numOfVowels += 1

print("Number of vowels: " + str(numOfVowels))

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))