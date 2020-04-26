"""
Assignment 7: Falling Apart
By: Lew Griffith

The task is to solve a kattis problem called "Falling Apart". Bob and Alice are separating and are dividing up the n pieces of their valued integer among each other. Each piece has a value, and they both want the pieces that have the most value. They are taking turns picking the pieces that they want, and Alice takes the first turn. 
"""
## Algorithm Steps ##
# Step 1: Have the user input the number of pieces on one line and store into a variable.
# Step 2: Have the user input the value of each piece on one line separated by a space. Store this string into a variable.
# Step 3: Split the string of values into individual strings and store them in a list.
# Step 4: Using a for-loop, covert each string in that list into an integer and store into another list.
# Step 5: Arrange this new list so that the values are listed from greatest to least.
# Step 6: Use a for-loop to have Alice and Bob take turns picking the greatest value from that list. Beginning at zero, Alice will have even numbered turns, and Bob will have odd numbered turns. Add up the total values distributed to each person.
# Step 7: After a piece has been picked, delete that element from the list so that it doesn't get picked again.
# Step 8: Print to the user on one line separated by a space the amounts aquired by Alice and Bob (in that order).
# Step 9: Create a function that tests if the program runs as it should using assert statements.

import sys

def kattis():
    # Step 1
    number_of_items = input()
    # Step 2
    values_of_items = input()
    # Step 8
    print(turn(values_of_items))

def turn(Svalues):
    Alice = 0
    Bob = 0
    # Step 3
    pieces = Svalues.split()
    values = []
    # Step 4
    for element in pieces:
        values.append(int(element))
    # Step 5
    values.sort(reverse = True)
    # Step 6
    for i in range(len(values)):
        if i % 2 == 0:
            Alice += values[0]
            # Step 7
            del values[0]
        else:
            Bob += values[0]
            # Step 7
            del values[0]
    return str(Alice) + ' ' + str(Bob)

# Step 9
def test():
    assert turn("23 55 66 1 6 323") == '384 90'
    assert turn("2 10 6 4 2") == "16 8"
    assert turn("5 5 5 5 5 5") == "15 15"
    print("All test cases passed!!")

if len(sys.argv) == 2 and sys.argv[1] == "test":
    test()
else:
    kattis()