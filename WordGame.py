#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    for ch in word:
        if letter == ch:
            return True
    """Returns boolean if letter is anywhere in the given word"""

    return False

def inSpot(letter, word, spot):
    correctLetter = word[spot]
    if letter == correctLetter:
        return True
    """Returns boolean response if letter is in the given spot in the word."""

    return False
 
def rateGuess(myGuess, word):

    feedback = ""

    for spot in range(5):
        myLetter = myGuess[spot]
        if inSpot(myLetter, word, spot) == True:
            feedback = feedback + myLetter.upper() #correct letter in location
        elif inWord(myLetter, word) == True:
            feedback = feedback + myLetter.lower() #correct letter in word, wrong spot
        else:
            feedback = feedback + "*"
    return feedback


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess
    guessNum = 1
    while guessNum <=6:
        #Ask user for their guess
        validWord = False
        while validWord == False:
            guess = input("Please enter a 5 letter word: ")
            guess = guess.lower()
            if guess not in wordList:
                print("Word not listed.")
                validWord = False
            else:
                validWord = True
        feedback = rateGuess(guess, todayWord)
        print(feedback)
        if feedback == todayWord.upper():
            print("Nice job!, you got it in ", guessNum, " tries!")
            break

        guessNum = guessNum + 1
        #Give feedback using on their word:
    print("The word was", todayWord)


    




if __name__ == '__main__':
  main()
