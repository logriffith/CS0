"""
Assignment 2: Area and Perimeter of a Triangle
By: Lew Griffith

The task is to write an algorithm using Python such that the computer will calculate the perimeter and area of a given triangle. We will also test to see if the inputed side lengths form a triangle.
"""

## To find the area and perimeter of a trianle, the user is required to imput lengths of three sides of a triangle.

print("Hello, would like to find the area and perimeter of a triangle? Please input\nthe lengths of the sides of the triangle without the units (i.e. numbers only).\nHowever, please make sure the side lengths are all in the same units.")
side1=input("What is the length of the first side?")
side2=input("What is the length of the second side?")
side3=input("What is the length of the thrid side?")

## Before we continue in the process, we need to make sure that these inputed lengths are positive real numbers. If not, then the program will not run.

if float(side1)>0 and float(side2)>0 and float(side3)>0:

## Since it doesn't make sense to compute the area and perimeter of a triangle if the given lengths don't even form a triangle, then we will next test to see if these lengths form a triangle using the Triangle Inequality. The Triangle Inequality states that if a and b are real numbers, then |a+b|<=|a|+|b|. We will use this fact to verify the lengths. If one combibation of sides a and b violates the Triangle Inequality, then these side lengths do not form a triangle.

    

## The units are also needed from the user.

    units=input("What are the units for these lengths?")

else:
    print("I am sorry, but positive real number lengths are needed here to calculate the area and perimeter.")