"""
Assignment 6: Avion
By: Lew Griffith

The task is to solve a kattis problem called "Avion". USKOK agents are looking for a corrupt government who plans to escape on a CIA blimp. CIA blimps have the string "FBI" somewhere in the registration codes. This program will allow the user to input 5 five registration codes (in rows) and will search for "FBI" in the string.
"""
# Algorithm Steps #
# 1. Get five rows of data from the user
# 2. Store the data into variables
# 3. Put data in a list
# 4. Search for "FBI" in each element of the list
# 5. If found, return the list indices plus 1 on one line, separated by a space, and in increasing order. If not, return "HE GOT AWAY".
# 6. Print the result to the user
# 7. Test its accuracy

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
    blimp=[b1,b2,b3,b4,b5]
    counter=0
    answer=''
    startSearch=0
# Step 4
    for code in blimp:
        if "FBI" in code:
            answer+=str(blimp.index(code,startSearch)+1)+' '
            startSearch+=1
        else:
            counter+=1
# Step 5
    if counter==5:
        return "HE GOT AWAY!"
    else:
        answer=answer.rstrip()
        return answer
# Step 7
def test():
    assert findBlimp("FBIuej","FBIdjfk","8","ueu","FBIkdkf")=="1 2 5"   
    assert findBlimp("mommy_dearest","Superman","Krypto","boombam","hi")=="HE GOT AWAY!"   
    assert findBlimp("hi","FBI11","FBI!","kdfkdjf", "graduation!!!!")=="2 3"
    print("All test cases passed!")

if len(sys.argv)==2 and sys.argv[1]=="test":   
    test()
else:
    c1,c2,c3,c4,c5=getBlimps()
# Step 6
    print(findBlimp(c1,c2,c3,c4,c5))


# To check to see if sample 1.in outputs the right answer when using the program, type cat 1.in | python3.7 avion.py | diff - 1.ans
# The cat command prints the content of the sample file
# By printing it into the program, the diff command compares the output to the sample output file (1.ans). If they match nothing happens, otherwise there is an error.
# Note cat and diff are linux commands.
# This saves typing in the sample input by hand.
