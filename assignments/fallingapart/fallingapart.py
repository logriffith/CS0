"""
Assignment 7: Falling Apart
By: Lew Griffith

The task is to solve a kattis problem called "Falling Apart". Bob and Alice are separating and are dividing up the n pieces of their valued integer among each other. Each piece has a value, and they both want the pieces that have the most value. They are taking turns picking the pieces that they want, and Alice takes the first turn. For every odd number <=n, Alice will choose the piece with the greatest value. For every even number <=n, Bob will choose the piece with the greatest value.
"""
## Algorithm Steps ##
# Step 1: Have the user input the number of pieces on one line and store into a variable.
# Step 2: Have the user input the value of each piece on one line separated by a space. Store data in a variable.
# Step 3: Split the string of values into individual strings and store in a list.
# Step 4: Covert each value from a string into a float and store into another list.
# Step 5: Use a for-loop to have Alice and Bob take turns.
# Step 6: Add up the total value distributed to each.
# Step 7: Print to the user on one line separated by a space the amounts aquired by Alice and Bob (in that order).

import sys

def turn(Svalues):
    Alice = 0
    Bob = 0
    pieces = Svalues.split()
    values = []
    for element in pieces:
        values.append(int(element))
    sortedValues = values.sort(reverse = True)
    for i in len(sortedValues):
        if i % 2 == 0:
            Alice += sortedValues[0]
            del sortedValues[0]
        else:
            Bob += sortedValues[0]
            del sortedValues[0]
    return str(Alice) + ' ' str(Bob)

def test():
    assert turn("23 55 66 1 6 323") == '384 90'
    assert turn("2 10 6 4 2") == "16 8"
    assert turn("5 5 5 5 5 5") == "15 15"

def kattis():
    number_of_items = input()
    values_of_items = input()
    return turn(values_of_items)

if len(sys.argv) == 2 and sys.argv[1] == "test":
    test()
else:
    kattis()

if len(sys.argv)==2 and sys.argv[1]=="test":   
    test()
else:
    c1,c2,c3,c4,c5=getBlimps()
print(turn('4 6644 66 12 11 1 5678')) 



