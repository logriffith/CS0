"""
Assignment 5: Guess the Number
By: Lew Griffith

The task is to write a Python program that will have the user play the typical game where the user has to guess a number in a specific range. In this game, the user will have to guess a number between 1 and 20.

"""
import random 
print()
print("Hello, welcome to the Guess the Number Game!")
print()
name=input("What is your name? ")
number=random.randint(1,20)
print("Hello,", name, "it is nice to meet you. I am thinking of a whole number between 1 and 20. Care to take a guess what it is? You can have up to 6 guesses.")
print(number)
for i in range(1,7):
    guess=int(input("What is your guess? "))
    if i==6 and guess!=number:
        if guess>number:
            print("Your guess is too high. This makes 6 attempts. You lose the game.")
        else:
            print("Your guess is too low. This makes 6 attempts. You lose the game.")
    elif guess>number:
        print("I am sorry, your guess is too high. Please take another guess.")
    elif guess<number:
        print("I am sorry, your guess is too low. Please take another guess.")
    elif guess==number:
        print("Congratulations,", name,"you win! You guessed the number in", i, "attempts.")
        break
    

