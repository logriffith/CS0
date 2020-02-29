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
        print("Cannot Divide by Zero")

def subtract(a,b):
    difference=a-b
    return difference

def modular(a,b):
    if b>0:
        mod=a%b
        return mod
    else:
        print("The second number must be greater than zero.")

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

### Assert Statements to Test Functions ###

#Sum Function#
assert sum(5,3)==8
assert sum(17,9)==26
#Multiply Function#
assert multiply(7,8)==56
assert multiply(0.5,10)==5
#Divide Function#
assert divide(125,5)==25
assert divide(41.54,5)==8.308
#Subtract Function#
assert subtract(37,9)==28
assert subtract(22.55,5.5)==17.05
#Modular Function#
assert modular(4,37)==4
assert modular(-4,7)==3
#Power Function#
assert power(0.5,3)==0.125
assert power(3,3)==27
#Square Root Function#
assert square_root(25)==5
assert square_root(0.25)==0.5
#Max Function#
assert max(33,656)==656
assert max(55,44)==55

print()
print("Hello, this program will provide the sum, difference, product, quotient,\nremainder (for integers), square root, and maximum of two numbers. In addition,\ngiven to numbers, this program will calculate the first number raised to the\npower of the second.")
print()
print("Please input the two numbers.")
numb1=input("What is the first number?")
numb2=input("What is the second number?")
print()
print("The sum of the two numbers is", sum(float(numb1),float(numb2)),'.')
print(modular(int(numb1),int(numb2)))