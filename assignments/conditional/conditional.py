"""
Assignment 4: Conditionals
By: Lew Griffith

The task is to write a Python program that computes certain values such as sum, product, max, min and average of any 5 given numbers. 
"""

def add(a,b,c,d,e):
    sum=a+b+c+d+e
    return sum

def multiply(a,b,c,d,e):
    product=a*b*c*d*e
    return product

def average(a,b,c,d,e):
    mean=add(a,b,c,d,e)/5
    return mean

def maximum(a,b,c,d,e):
    