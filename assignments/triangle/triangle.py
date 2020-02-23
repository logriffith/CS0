"""
Assignment 2: Area and Perimeter of a Triangle
By: Lew Griffith

The task is to write an algorithm using Python such that the computer will calculate the perimeter and area of a given triangle. We will also test to see if the inputed side lengths form a triangle.
"""
## The math library will be needed to use the squart root function later.
import math

## The following is a function that will be used later:
def is_triangle(a,b,c):
    if (a+b)>c and (a+c)>b and (b+c)>a:
        return True
    else:
        return False

## To find the area and perimeter of a trianle, the user is required to imput lengths of three sides of a triangle.
print()
print("Hello, would like to find the area and perimeter of a triangle? Please input\nthe lengths of the sides of the triangle without the units (i.e. numbers only).\nHowever, please make sure the side lengths are all in the same units.")
print()
side1=input("What is the length of the first side?")
side2=input("What is the length of the second side?")
side3=input("What is the length of the thrid side?")
print()

## Before we continue in the process, we need to make sure that these inputed lengths are positive real numbers. If not, then the program will not run. Also, it doesn't make sense to compute the area and perimeter of a triangle if the given lengths don't even form a triangle. Thus, we will next test to see if these lengths form a triangle using the Triangle Inequality. The Triangle Inequality states that if a and b are real numbers, then |a+b|<=|a|+|b|. Geometrically, this means that the sum of any two side lengths of a triangle must by greater than the third. We will use this fact to verify the lengths. If one combibation of sides a and b violates the Triangle Inequality, then these sides do not form a triangle. Note that the is_triangle function defined above uses the Triangle Inequality to verify that the given sides form a triangle.

if float(side1)>0 and float(side2)>0 and float(side3)>0 and is_triangle(float(side1),float(side2),float(side3))==True:

## The units are also needed from the user.

    units=input("What are the units for these lengths?")
    perimeter=float(side1)+float(side2)+float(side3)
    print()

## We don't know which of the three sides is the bass nor do we know the height of the triangle. Thus, we will use Heron’s formula to calculate the area of the triangle. This formula states that the area of a triangle is the square of the product p(p-side1)(p-side2)(p-side3), where p is half of the triangles perimeter.

    area=math.sqrt((perimeter/2)*((perimeter/2)-float(side1))*((perimeter/2)-float(side2))*((perimeter/2)-float(side3)))
    print("Here are your results:")
    print("\tThe perimeter of this triangle is" , perimeter , units , '.')
    print("\tThe area of this triangle is" , area , "square" , units , '.')
    print()
    print("Let's verify that the three sides form a triangle. If it is, then the sum\nof any two side lengths will be greater than the third.")
    print()
    if is_triangle(float(side1),float(side2),float(side3))==True:
        print("Yes, these sides form a triangle.")
    else:
        print("No, these sides do not form a triangle.")
else:
    print("I am sorry, but positive real number lengths of a triangle are needed here to calculate the area and perimeter.")