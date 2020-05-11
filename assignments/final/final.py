"""
Final Project: Hangman Game
By: Lew Griffith

This program is the Hangman Game. The rules of the game are to guess a letter in a random word from a text file. Note that each word is all lower case. If the suggested letter is not in the word, then a head is drawn. Each guessed letter that is not in the word will result in another limb being drawn. If the user fiqures out the word by finding all of its letters before the stick figure is complete, then they win, otherwise, they lose.

"""
import random

# gallows functions print each of the stages
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
        data = wordsFile.readlines() # puts the words from the text file into a list
    for element in data:
        wordsList.append(element.strip()) # removes the \n from the end of each word and stores the words into another list
    word = random.randint(0,len(wordsList)-1) # pick a random index for this list
    gallows0() # show the user the empty gallows
    for i in range(len(wordsList[word])):
        print('_ ', end=' ') # show the user how many letters are in this word
    print('\n')
    counter = 0 # this will be the variable that stores how many mistakes were made
    characters = 0 # this will be the variable that stores how many letters have been found
    while characters <= len(wordsList[word]): 
        if characters == len(wordsList[word]):
            print("You Won!") # you win if you find all of the letters in the word
            break
        elif counter == 6:
            print("You lose! Why did you have to let him die?")
            break
        guess=input("What is your guess? ")
        if guess in wordsList[word] and counter <= 6:
            characters += wordsList[word].count(guess) # keep a running total of how many letters have been found
            for i in range(len(wordsList[word])):
                if wordsList[word][i] == guess:
                    print(guess, end=' ') # if letters have been found, show where they are in the word
                else: 
                    print('_', end=' ')
            print('\n')
        elif guess not in wordsList[word] and counter <= 6:
            counter += 1
            # each time you guess wrong, another limb is drawn
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
print("\nWelcome to the Hangman game! A word has been randomly selected from a text file.\nCan you figure out what the word is? Guess letters you think are in the word. At\n6 mistakes, the full stick figure is drawn at the Gallows. If you make 6 mistakes\nbefore figuring out what the word is, you lose. Please only input lower case\nEnglish letters.") 
answer = 'y'   
while answer == 'y':  
    game()
    answer = input("Would you like to play again? [y or n] ")

