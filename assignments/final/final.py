"""
Final Project: Hangman Game
By: Lew Griffith

This program is the Hangman Game. The rules of the game are to guess a letter in a random word from a text file. Note that each word is all lower case. If the suggested letter is not in the word, then a head is drawn. Each guessed letter that is not in the word will result in another limb being drawn. If the user fiqures out the word before they reach Stage 6, then they win, otherwise, they lose.

"""
import random

def gallows0():
    print('\n\tThe Gallows\n')
    print('\t|---------|')
    print('\t|/        |')
    print('\t|')
    print('\t|')
    print('\t|')
    print('\t|')
    print('\t|')
    print('\t-------------')
def gallows1():
    print('\n\tThe Gallows\n')
    print('\t|---------|')
    print('\t|/        |')
    print('\t|         O')
    print('\t|')
    print('\t|')
    print('\t|')
    print('\t|')
    print('\t-------------')
def gallows2():
    print('\n\tThe Gallows\n')
    print('\t|---------|')
    print('\t|/        |')
    print('\t|         O')
    print('\t|         |')
    print('\t|         |')
    print('\t|')
    print('\t|')
    print('\t-------------')
def gallows3():
    print('\n\tThe Gallows\n')
    print('\t|---------|')
    print('\t|/        |')
    print('\t|         O')
    print('\t|        \\|')
    print('\t|         |')
    print('\t|')
    print('\t|')
    print('\t-------------')
def gallows4():
    print('\n\tThe Gallows\n')
    print('\t|---------|')
    print('\t|/        |')
    print('\t|         O')
    print('\t|        \\|/')
    print('\t|         |')
    print('\t|')
    print('\t|')
    print('\t-------------')
def gallows5():
    print('\n\tThe Gallows\n')
    print('\t|---------|')
    print('\t|/        |')
    print('\t|         O')
    print('\t|        \\|/')
    print('\t|         |')
    print('\t|        /')
    print('\t|')
    print('\t-------------')
def gallows6():
    print('\n\tThe Gallows\n')
    print('\t|---------|')
    print('\t|/        |')
    print('\t|         O')
    print('\t|        \\|/')
    print('\t|         |')
    print('\t|        / \\')
    print('\t|')
    print('\t-------------')
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
    while counter < 6:
        guess=input("What is your first guess?")
        if guess in wordsList[word] and counter == 0:
            characters += wordsList[word].count(guess)
            guess1 = guess
            gallows0()
            for i in range(len(wordsList[word])):
                if wordsList[word][i] == guess1:
                    print(guess1, end=' ')
                else: 
                    print('_', end=' ')
                print('\n')
        elif guess not in wordsList[word] and counter == 0:
            counter += 1
            gallows1()
            for i in range(len(wordsList[word])):
                print('_ ', end=' ')
            print('\n')
        elif guess in wordsList[word] and counter == 1:
            characters += wordsList[word].count(guess)
            guess2 = guess
            gallows1()
            for i in range(len(wordsList[word])):
                if wordsList[word][i] == guess1:
                    print(guess1, end=' ')
                if wordsList[word][i] == guess2:
                    print(guess2, end=' ')
                else: 
                    print('_', end=' ')
                print('\n')
            
#game()

