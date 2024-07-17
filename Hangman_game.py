#Hangman game by Virginia Herrero

import random
from pathlib import Path

WORDLIST_FILENAME = "hangman_words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters
    """

    #Search the file in the correct directory
    data_file_path = Path(__file__).parent / WORDLIST_FILENAME
    print("Loading word list from file...")
    #inFile: file
    inFile = open(data_file_path, 'r')
    #line: string
    line = inFile.readline()
    #wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


#Load the list of words into the variable wordlist so that it can be accessed from anywhere in the program

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are lowercase
    letters_guessed: list (of letters), which letters have been guessed so far; assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed; False otherwise
    """
    
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents which letters in secret_word have been guessed so far.
    """
    
    guess = " "
    for letter in secret_word:
        if letter in letters_guessed:
            guess += letter
        else:
            guess += "_"
    return guess


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not yet been guessed.
    """
    
    not_guessed= " "
    abc = "abcdefghijklmnñopqrstuvwxyz"
    for letter in abc:
        if letter not in letters_guessed:
            not_guessed += letter
    return not_guessed
    

def hangman(secret_word):
    """
    secret_word: string, the secret word to guess
    
    Interactive Hangman game:
    
    * At the start of the game, it is displayed how many letters the secret_word contains and how many guesses they start with
      
    * The user starts with 6 guesses and 3 warnings

    * Before each round, it is displayed how many guesses they have left and the letters that the user has not yet guessed
    
    * Ask the user to supply one guess per round. If they dont enter a valid letter, they get a warning
    
    * The user receives feedback immediately after each guess about whether their guess appears in the secret_word

    * After each guess, the partially guessed word is displayed to the user
    """
    
    num_guesses = 6
    num_warnings = 3
    letters_guessed = []
    vowels = "aeiou"
   
    print("-----------")
    print("Welcome to the Hangman game!")
    print("Game instructions:")
    print("- You have to guess the secret word")
    print("- You have 6 chances to guess it before the game is over")
    print("- If you guess a vowel wrong: you lose two chances to guess it")
    print("- If you guess a consonant wrong: you only lose a chance to guess it")
    print("- You are given 3 warnings")
    print("- If you type a non alphabetical character or a repeated letter, you get a warning")
    print("- When you run out of warnings, you lose a chance to guess the secret word")
    print("- The game ends either when you guess the secret word correctly or when you run out of chances to guess it")
    print("----------")
    print("Find the secret word in less than 6 tries and you win!")
    print("Ready, set, go!")
    print("----------")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have", num_warnings, "warnings left")

    while is_word_guessed(secret_word, letters_guessed) is not True:
      if num_guesses == 0:
          break
      print("You have", num_guesses, "guesses left")
      print("Available letters:", get_available_letters(letters_guessed))
      guess = input("Please guess a letter: ").lower()
      guessed_word = get_guessed_word(secret_word, letters_guessed)

      if guess.isalpha():
          if guess not in letters_guessed:
              letters_guessed.append(guess)
              guessed_word = get_guessed_word(secret_word,letters_guessed)
              if guess in secret_word:
                  print("Good guess!")
                  print("The secret word:", guessed_word)
              else:
                  if guess in vowels:
                      num_guesses -= 2
                      print("Oops! That vowel is not in the secret word and you lose two chances to guess. You have", num_guesses, "guesses left")
                      print("The secret word:", guessed_word)
                  else:
                      num_guesses -= 1
                      print("Oops! That letter is not in the secret word and you lose a chance to guess. You have", num_guesses, "guesses left")
                      print("The secret word:", guessed_word)
          else:
              if num_warnings > 0:
                  num_warnings -= 1
                  print("Oops! You've already guessed that letter. You have", num_warnings, "warnings left")
                  print("The secret word:", guessed_word)
              else:
                  num_guesses -= 1
                  print("Oops! You've already guessed that letter. You now have no warnings and you lose one guess. You have", num_guesses, "guesses left")
                  print("The secret word:", guessed_word)
      else:
          if num_warnings > 0:
              num_warnings -= 1
              print("Oops!That is not a valid letter. You have", num_warnings, "warnings left")
              print("The secret word:", guessed_word)
          else:
              num_guesses -= 1
              print("Oops! That is not a valid letter. You now have no warnings and you lose one guess. You have", num_guesses, "guesses left")
              print("The secret word:", guessed_word)

      print("-------------")

      if is_word_guessed(secret_word, letters_guessed):
        unique_letters_in_secret_word = []
        for char in secret_word:
          if char not in unique_letters_in_secret_word:
            unique_letters_in_secret_word.append(char)
        print("Congratulations, you guessed the secret word! You won!")
        break
    
      if num_guesses <= 0:
        print("Sorry, you ran out of guesses. The secret word was {}".format(secret_word))
        break
    
if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)

