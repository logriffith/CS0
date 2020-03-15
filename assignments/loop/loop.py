"""
Assignment 5: Guess the Number
By: Lew Griffith

The task is to write a Python program that will have the user play the typical game where the user has to guess a number in a specific range. In this game, the user will have to guess a whole number between 1 and 20 (i.e. 1<=number<=20). The user can have up to 6 guesses. If the user guesses the number within 6 attempts, they win. Otherwise, they will lose the game. To help the user make better guesses, the user will be informed if their guess is too high or too low. The user can have the program continue to run until they decide that they don't want to play anymore.

"""
import random 
answer='y'
game_played=0
lost=0
won=0
print()
print("Hello, welcome to the Guess the Number Game!")
print()
name=input("What is your name? ")
print()
print("Hello,", name, "it is nice to meet you.")
print()
while answer=='y':
    print("I am thinking of a whole number between 1 and 20. Care to take a guess what it is?\nYou can have up to 6 guesses.")
    print()
    number=random.randint(1,20)
    for i in range(1,7):
        guess=int(input("What is your guess? "))
        if i==6 and guess!=number:
            if guess>number:
                print("Your guess is too high. This makes 6 attempts. You lose the game. \nThe number was", number,'.')
                print()
            else:
                print("Your guess is too low. This makes 6 attempts. You lose the game. \nThe number was", number,'.')
                print()
            game_played+=1
            lost+=1
        elif guess>number:
            print("I am sorry, but your guess is too high. Please make another guess.")
            print()
        elif guess<number:
            print("I am sorry, but your guess is too low. Please make another guess.")
            print()
        elif guess==number:
            print("Congratulations,", name,"you win!!! The number is indeed", number, ".\nYou guessed the number in", i, "attempt(s).")
            game_played+=1
            won+=1
            print()
            break
    answer=input("Would you like to play again? [y or n] ")
print()
print("Here are your stats:")
print("\tThe game was played", game_played, "time(s).")
print("\tYou won the game", won, "time(s).")
print("\tYou lost the game", lost, "time(s).")