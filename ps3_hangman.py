# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    lettersSecretWord = list(secretWord)
    stringLettersGuessed = ''.join(lettersGuessed)
    for letter in lettersSecretWord:
        if not letter in stringLettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = []
    lettersSecretWord = list(secretWord)
    stringLettersGuessed = ''.join(lettersGuessed)
    for letter in lettersSecretWord:
        if letter in stringLettersGuessed:
          result.append(letter)
        else:
          result.append("_")

    return ''.join(result)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    allLettersList = list(string.ascii_lowercase)
    for letter in lettersGuessed:
      allLettersList.remove(letter)

    return ''.join(allLettersList)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.

    Example of messages:
    Welcome to the game Hangman!
    I am thinking of a word that is 4 letters long.
	  -------------
	  You have 8 guesses left.
	  Available letters: abcdefghijklmnopqrstuvwxyz
	  Please guess a letter: a
	  Good guess: _ a_ _
	  ------------
    '''
    # FILL IN YOUR CODE HERE...
    import string

    welcomeMessage = "Welcome to the game Hangman!"
    messageLengthOfWord = "I am thinking of a word that is {} letters long"
    spacer = "-------------"
    messageGuessesLeft = "You have {} guesses left."
    messageAvailableLetters = "Available letters: {}"
    inputGuessALetter = "Please guess a letter: "
    messageGoodGuess = "Good guess: {}"
    messageAlreadyGuessed = "Oops! You've already guessed that letter: {}"
    messageNotInWord = "Oops! That letter is not in my word: {}"
    messageCongrats = "Congratulations, you won!"
    messageSorryLoser = "Sorry, you ran out of guesses. The word was {}."

    lettersCorrectlyGuessed = []
    allLettersGuessed = []
    guessesLeft = 8
    availableLetters = string.ascii_lowercase

    print(welcomeMessage)
    print(messageLengthOfWord.format((len(secretWord))))
    print(spacer)

    while guessesLeft > 0 and not isWordGuessed(secretWord, lettersCorrectlyGuessed):
      print(messageGuessesLeft.format((guessesLeft)))
      print(messageAvailableLetters.format((availableLetters)))
      guessedInput = input(inputGuessALetter)
      guessInLowerCase = guessedInput.lower()

      if guessInLowerCase and guessInLowerCase not in availableLetters:
        print(messageAlreadyGuessed.format(getGuessedWord(secretWord, lettersCorrectlyGuessed)))
      else:

        if guessInLowerCase and guessInLowerCase in secretWord:
          lettersCorrectlyGuessed.append(guessInLowerCase)
          allLettersGuessed.append(guessInLowerCase)
          print(messageGoodGuess.format(getGuessedWord(secretWord, lettersCorrectlyGuessed)))
          availableLetters = getAvailableLetters(allLettersGuessed)
        else:
          if guessInLowerCase:
            allLettersGuessed.append(guessInLowerCase)
            availableLetters = getAvailableLetters(allLettersGuessed)
            print(messageNotInWord.format(getGuessedWord(secretWord, lettersCorrectlyGuessed)))
            guessesLeft -= 1

      print(spacer)

    if guessesLeft == 0:
      print(messageSorryLoser.format(secretWord))
    elif isWordGuessed(secretWord, lettersCorrectlyGuessed):
      print(messageCongrats)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
# secretWord = "xavier"
hangman(secretWord)
