"""
Assignment 3: A Basic Calculator using Functions and Automated Unit Testing
By: Lew Griffith

The task is to write a Python program that performs some arithmetic operations on two given numbers. These numbrers will be inputed by the user.

"""

import math


def sum(a,b):
    sum=a+b
    return sum

def multiply(a,b):
    product=a*b
    return product

def divide(a,b):
    if b!=0:
        quotient=a/b
        return quotient
    else:
        print("Error: Cannot Divide by Zero")

def subtract(a,b):
    difference=a-b
    return difference

def modular(a,b):
    if b!=0:
        mod=a%b
        return mod
    else: 
        print("Error: Cannot Divide by Zero")

def power(a,b):
    if b==0:
        return 1
    else:
        answer=a**b
        return answer

def square_root(a):
    if a>=0:
        root=math.sqrt(a)
        return root
    else:
        print("Not a real number")




