"""
Assignment 3: A Basic Calculator using Functions and Automated Unit Testing
By: Lew Griffith

The task is to write a Python program that performs some arithmetic operations on two given numbers. These numbrers will be inputed by the user. Functions were created in order to make the desired calculations.

"""
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
        print("Cannot divide by zero.")

def power(a,b):
    if b==0:
        return 1
    else:
        answer=a**b
        return answer

def square_root(a):
    if a>=0:
        root=power(a,0.5)
        return root
    else:
        print("Not a real number")

#Bonus Function
def max(a,b):
    if a<b:
        return b
    elif a>b:
        return a
    else:
        print("They are equal")

assert sum(5,3)==8
assert sum(17,9)==26

print()
print("Hello, this program will provide the sum, difference, product, quotient,\nremainder (for integers), square root, and maximum of two numbers. In addition,\ngiven to numbers, this program will calculate the first number raised to the\npower of the second.")
print()
print("Please input the two numbers.")
numb1=input("What is the first number?")
numb2=input("What is the second number?")
print()
print("The sum of the two numbers is", sum(float(numb1),float(numb2)),'.')
print(modular(int(numb1),int(numb2)))