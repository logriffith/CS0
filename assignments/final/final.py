"""
Final Project: Hangman Game
By: Lew Griffith

This program is the Hangman Game. The rules of the game are to guess a letter in a random word from a text file. Note that each word is all lower case. If the suggested letter is not in the word, then a head is drawn. Each guessed letter that is not in the word will result in another limb being drawn. If the user fiqures out the word before they reach Stage 6, then they win, otherwise, they lose.

"""
import random

def gallows0():
    print('\nThe Gallows\n')
    print('|---------|')
    print('|/        |')
    print('|')
    print('|')
    print('|')
    print('|')
    print('|')
    print('-------------')
def gallows1():
    print('\nThe Gallows\n')
    print('|---------|')
    print('|/        |')
    print('|         O')
    print('|')
    print('|')
    print('|')
    print('|')
    print('-------------')
def gallows2():
    print('\nThe Gallows\n')
    print('|---------|')
    print('|/        |')
    print('|         O')
    print('|         |')
    print('|         |')
    print('|')
    print('|')
    print('-------------')
def gallows3():
    print('\nThe Gallows\n')
    print('|---------|')
    print('|/        |')
    print('|         O')
    print('|        \\|')
    print('|         |')
    print('|')
    print('|')
    print('-------------')
def gallows4():
    print('\nThe Gallows\n')
    print('|---------|')
    print('|/        |')
    print('|         O')
    print('|        \\|/')
    print('|         |')
    print('|')
    print('|')
    print('-------------')
def gallows5():
    print('\nThe Gallows\n')
    print('|---------|')
    print('|/        |')
    print('|         O')
    print('|        \\|/')
    print('|         |')
    print('|        /')
    print('|')
    print('-------------')
def gallows6():
    print('\nThe Gallows\n')
    print('|---------|')
    print('|/        |')
    print('|         O')
    print('|        \\|/')
    print('|         |')
    print('|        / \\')
    print('|')
    print('-------------')
def game():
    wordsList = []
    with open('words.txt', 'r') as wordsFile:
        data = wordsFile.readlines()
    for element in data:
        wordsList.append(element.strip())
    word = random.randint(0,len(wordsList)-1)
    gallows0()
    for i in range(len(wordsList[word])):
        print('_ ', end=' ')
    print('\n')
    counter = 0
    characters = 0
    while characters <= len(wordsList[word]):
        if characters == len(wordsList[word]):
            print("You Won!")
            break
        elif counter == 6:
            print("You lose!")
            break
        guess=input("What is your guess?")
        if guess in wordsList[word] and counter <= 6:
            characters += wordsList[word].count(guess)
            for i in range(len(wordsList[word])):
                if wordsList[word][i] == guess:
                    print(guess, end=' ')
                else: 
                    print('_', end=' ')
            print('\n')
        elif guess not in wordsList[word] and counter <= 6:
            counter += 1
            if counter == 1:
                gallows1()
            elif counter == 2:
                gallows2() 
            elif counter == 3:
                gallows3() 
            elif counter == 4:
                gallows4() 
            elif counter == 5:
                gallows5()
            elif counter == 6:
                gallows6()  
    
        
game()

