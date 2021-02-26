#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:10:24 2021

@author: cgarate
"""

# Remaining balance: 813.41
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

def calcMonthlyInterestRate (annualInterestRate):
    return annualInterestRate / 12.0

def calcMinimumMonthlyPayment (monthlyPaymentRate, balance):
    return monthlyPaymentRate * balance

def calcMonthlyUnpaidBalance (balance, minimumPayment):
    return balance - minimumPayment


def ccBalanceWithMinimumPaymentRate (balance, annualInterestRate, monthlyPaymentRate):
    resultString = "Remaining balance: {:.2f}"
    checkStepOutput = "Month {} Remaining balance: {:.2f}"
    monthlyInterestRate = calcMonthlyInterestRate(annualInterestRate)
    for i in range(0,12):
        mininumPayment = calcMinimumMonthlyPayment(monthlyPaymentRate, balance)
        unpaidBalance = calcMonthlyUnpaidBalance(balance, mininumPayment)
        interest = monthlyInterestRate * unpaidBalance
        balance = unpaidBalance + interest
        print(checkStepOutput.format(i+1,balance))
        
    print(resultString.format(balance))
    return balance

def ccBalanceWithMinimumFixedPayment (balance, annualInterestRate, monthlyFixedPayment):
    resultString = "Remaining balance: {:.2f}"
    checkStepOutput = "Month {} Remaining balance: {:.2f}"
    monthlyInterestRate = calcMonthlyInterestRate(annualInterestRate)
    for i in range(0,12):
        unpaidBalance = calcMonthlyUnpaidBalance(balance, monthlyFixedPayment)
        interest = monthlyInterestRate * unpaidBalance
        balance = unpaidBalance + interest
        #print(checkStepOutput.format(i+1,balance))
        
    #print(resultString.format(balance))
    return balance


# Lowest Payment: 180 
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
def minimumFixedPayment (balance, annualInterestRate):
    resultString = "Lowest Payment: {}"
    initialBalance = balance
    initialFixedPayment = 10
    while True:
        balanceAtEOY = ccBalanceWithMinimumFixedPayment(balance, annualInterestRate, initialFixedPayment)
        if balanceAtEOY <= 0:
            break
        else:
            initialFixedPayment += 10
        
    #print(resultString.format(initialFixedPayment))
    return initialFixedPayment
    

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

def minimumFixedPaymentBisection (balance, annualInterestRate):
    resultString = "Lowest Payment: {:.2f}"
    monthlyInterestRate = calcMonthlyInterestRate(annualInterestRate)
    paymentLowerBound = balance / 12
    paymentUpperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
    midpoint = (paymentLowerBound + paymentUpperBound) / 2
    epsilon = 0.1
    
    while True:
        balanceAtEOY = ccBalanceWithMinimumFixedPayment(balance, annualInterestRate, midpoint)
        
        if balanceAtEOY == 0 or (balanceAtEOY > 0 and balanceAtEOY <= epsilon):
            break
        
        if balanceAtEOY > epsilon:
            paymentLowerBound = midpoint
            
        if balanceAtEOY < 0:
            paymentUpperBound = midpoint

        
        midpoint = (paymentLowerBound + paymentUpperBound) / 2
        


    print(resultString.format(midpoint))
    print(balanceAtEOY == 0)
    return midpoint
            
        
    
minimumFixedPaymentBisection(999999,0.18)