#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:20:45 2021

@author: cgarate
"""


low = 0
high = 100
midPoint = int(high / 2)
validOptions = ['h', 'l', 'c']
questionSecretNumber = "Is your secret number "
instructions = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "
comeAgain = "Sorry, I did not understand your input."
gameOver = "Game over. Your secret number was: "
intro = "Please think of a number between 0 and 100!"

print(intro)
print(questionSecretNumber + str(midPoint) + '?')
userInput = str(input(instructions))

while True:
    if userInput not in validOptions:
        print(comeAgain)
        print(questionSecretNumber + str(midPoint) + '?')
        userInput = str(input(instructions))
    else:
        if userInput == 'h':
            high = midPoint
        elif userInput == 'l':
            low = midPoint
        elif userInput == 'c':
            print(gameOver + str(midPoint))
            break

        midPoint = int((high + low) / 2)
        print(questionSecretNumber + str(midPoint) + '?')
        userInput = str(input(instructions))