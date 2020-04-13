"""
Assignment 5: Avion
By: Lew Griffith

The task is to solve a kattis problem called "Avion". USKOK agents are looking for a corrupt government who plans to escape on a CIA blimp. CIA blimps have the string "FBI" somewhere in the registration codes. This program will allow the user to input 5 five registration codes (in rows) and will search for "FBI" in the string.
"""
# Algorithm Steps #
# 1. Get the data from the user
# 2. Store the data in variables
# 3. Search for "FBI" in each string
# 4. If found, return the row number on one line separated by a space each and in increasing order. If not, return "HE GOT AWAY".
# 5. Print the result
# 6. Test its accuracy

import sys

def getBlimps():
# Steps 1 and 2
    b1=input()
    b2=input()
    b3=input()
    b4=input()
    b5=input()
    return b1,b2,b3,b4,b5

def findBlimp(b1,b2,b3,b4,b5):
# Step 3
    if b1.find("FBI")<0 and b2.find("FBI")<0 and b3.find("FBI")<0 and b4.find("FBI")<0 and b5.find("FBI")<0:
        answer="HE GOT AWAY!"
        return answer
    else: 
        
# Step 6
def test():
    assert findBlimp("FBIuej","FBIdjfk","8","ueu","FBIkdkf")=="1 2 5"   
    assert findBlimp("mommy_dearest","Superman","Krypto","boombam","hi")=="HE GOT AWAY!"   
    assert findBlimp("hi","FBI11","FBI!","kdfkdjf", "graduation!!!!")=="2 3"
    print("All test cases passed")

if len(sys.argv)==2 and sys.argv[1]=="test":
    test()
else:
# Step 5
   if "FBI" in "dkfjdFBIdfjdkj":
       print("It worked")
