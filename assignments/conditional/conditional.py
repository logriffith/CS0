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

def average5(a,b,c,d,e):
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

def main():
    print("Hello, please enter five numbers to compute the sum, product, average, maximum, and minimum.")
    print()
    numb1=input("What is the first number? ")
    numb2=input("What is the second number? ")
    numb3=input("What is the third number? ")
    numb4=input("What is the fourth number? ")
    numb5=input("What is the fifth number? ")
    print()
    print("The sum of these numbers is", add(numb1,numb2,numb3,numb4,numb5))
    print("The product of these numbers is", multiply(numb1,numb2,numb3,numb4,numb5))
    print("The average of these numbers is", average5(numb1,numb2,numb3,numb4,numb5))
    print("The maximum number is", maximum(numb1,numb2,numb3,numb4,numb5))
    print("The minimum number is", minimum(numb1,numb2,numb3,numb4,numb5))

def test():
    assert add(2,2,2,2,2)==10
    assert add(23,34.6,45,35.04,688.004)==825.644
    assert multiply(1,99,1,1,1)==99
    assert multiply(4,5,3,7,11)==4620
    assert average5(17,30,27,20,23)==23.4
    assert average5(87,99,80,95,90)==90.2
    assert maximum(4,5,6,7,77)==77
    assert maximum(123,233,434,553,484848)==484848
    assert minimum(4,5,6,7,77)==4
    assert minimum(-5,3,5,6,4)==-5

