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
    if a>b and a>c and a>d and a>e:
        return a
    elif b>a and b>c and b>d and b>e:
        return b
    elif c>a and c>b and c>d and c>e:
        return c
    elif d>a and d>b and d>c and d>e:
        return d
    elif e>a and e>b and e>c and e>d:
        return e
    else:
        print("Could not find a maximum.")

def minimum(a,b,c,d,e):
    if a<b and a<c and a<d and a<e:
        return a
    elif b<a and b<c and b<d and b<e:
        return b
    elif c<a and c<b and c<d and c<e:
        return c
    elif d<a and d<b and d<c and d<e:
        return d
    elif e<a and e<b and e<c and e<d:
        return e
    else:
        print("Could not find a minimum.")