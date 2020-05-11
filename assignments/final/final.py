"""
Final Project: Hangman Game
By: Lew Griffith

This program is the Hangman Game. The rules of the game are to guess a letter in a random word from a text file. Note that each word is all lower case. If the suggested letter is not in the word, then a head is drawn. Each guessed letter that is not in the word will result in another limb being drawn. If the user fiqures out the word before they reach Stage 6, then they win, otherwise, they lose.

"""
import random

def game():
    wordsList = []
    with open('words.txt', 'r') as wordsFile:
        data = wordsFile.readlines()
    for element in data:
        wordsList.append(element.strip())
    word = random.randint(0,len(wordsList)-1)
    print('\n\tGallows\n')
    print('\t|---------|')
    print('\t|/        |')
    print('\t|')
    print('\t|')
    print('\t|')
    print('\t|')
    print('\t|')
    print('\t-------------')
    for i in range(len(wordsList[word])):
        print('_ ', end=' ')
    print()
    print()
    guess1=input("What is your first guess?")
    if guess1 in wordsList[word]:
        print('\n\tGallows\n')
        print('\t|---------|')
        print('\t|/        |')
        print('\t|')
        print('\t|')
        print('\t|')
        print('\t|')
        print('\t|')
        print('\t-------------')
        for i in range(len(wordsList[word])):
            if wordsList[word][i] == guess1:
                print(guess1, end=' ')
            else: 
                print('_', end=' ')
    else:
        print('\n\tGallows\n')
        print('\t|---------|')
        print('\t|/        |')
        print('\t|         O')
        print('\t|')
        print('\t|')
        print('\t|')
        print('\t|')
        print('\t-------------')
        for i in range(len(wordsList[word])):
            print('_ ', end=' ')
        print()

game()
"""

print("Stage 2")
print()
print('\t|---------|')
print('\t|/        |')
print('\t|         O')
print('\t|         |')
print('\t|         |')
print('\t|')
print('\t|')
print('\t|')
print('\t-------------')
print()
print("Stage 3")
print()
print('\t|---------|')
print('\t|/        |')
print('\t|         O')
print('\t|        \\|')
print('\t|         |')
print('\t|')
print('\t|')
print('\t|')
print('\t-------------')
print()
print("Stage 4")
print()
print('\t|---------|')
print('\t|/        |')
print('\t|         O')
print('\t|        \\|/')
print('\t|         |')
print('\t|')
print('\t|')
print('\t|')
print('\t-------------')
print()
print("Stage 5")
print()
print('\t|---------|')
print('\t|/        |')
print('\t|         O')
print('\t|        \\|/')
print('\t|         |')
print('\t|        /')
print('\t|')
print('\t|')
print('\t-------------')
print()
print("Stage 6")
print()
print('\t|---------|')
print('\t|/        |')
print('\t|         O')
print('\t|        \\|/')
print('\t|         |')
print('\t|        / \\')
print('\t|')
print('\t|')
print('\t-------------')
"""