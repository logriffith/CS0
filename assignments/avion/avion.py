"""
Assignment 5: Avion
By: Lew Griffith

The task is to solve a kattis problem called "Avion". USKOK agents are looking for a corrupt government who plans to escape on a CIA blimp. CIA blimps have the string "FBI" somewhere in the registration codes. This program will allow the user to input 5 five registration codes (in rows) and will search for "FBI" in the string.
"""
# Algorithm Steps #
# 1. Get the data from the user
# 2. Store the data in variables
# 3. Search for "FBI" in each string
# 4. If found, output the row number on one line separated by a space each and in increasing order
# 5. If not, output "HE GOT AWAY"

def getBlimps():
# Steps 1 and 2
    b1=input()
    b2=input()
    b3=input()
    b4=input()
    b5=input()
    return [b1,b2,b3,b4,b5]

def findBlimp():
    blimp=getBlimps()
    #for code in blimp:
    #    if code.find("FBI")>=0:
    #        print(blimp.index(code), end='')
    print(blimp)

findBlimp()
hey=[1,5,6,3]
print(hey.index(6))