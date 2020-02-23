"""
Assignment 2: Area and Perimeter of a Triangle
By: Lew Griffith

The task is to write an algorithm using Python such that the computer will calculate the perimeter and area of a given triangle. We will also test to see if the inputed side lengths form a triangle.
"""

## To find the area and perimeter of a trianle, the user is required to imput lengths of three sides of a triangle.

print("Hello, would like to find the area and perimeter of a triangle? Please input the lengths of the sides of the triangle without the units (i.e. numbers only). However, please make sure the side lengths are all in the same units.")
side1=input("What is the length of the first side?")
side2=input("What is the length of the second side?")
side3=input("What is the length of the thrid side?")

## The units are also needed from the user.

units=input("What are the units for these lengths?")