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

def getData():
    pieces = int(input())
    values = [input() for piece in range(pieces)]
    return values

print(type(5.0))
print(type(5))
if 5==5.0:
    print("Okay that worked")
else:
    print("They are not equal!")