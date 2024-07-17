# Hangman
![GitHub top language](https://img.shields.io/github/languages/top/herrerovir/hangman-game)


Hangman is a classic word-guessing game where players must guess a secret word one letter at a time. 

This project is a simple implementation of the game in Python. The game randomly chooses a word from a list of words and asks the player to guess the letters of the secret word until the player correctly guesses it or runs out of chances to guess it. 

The code consists of two files: Hangman_game.py and Hangman_words.txt. Both files must be stored in the same directory, otherwise the program will not work. 

## Dependencies:

Python 3

Libraries used: random, pathlib

## How to run the script:

* Clone or download the repository to your local machine

* Run the Hangman_game.py file in a Python environment

* Enjoy the game!

## How to play:

* The game will choose a random word from the list of words provided

* You have 6 chances to guess the secret word correctly

* The games asks you to guess a letter:

	* if the guessed letter is in the secret word, it will be revealed in the correct position(s) in the secret word
	* if the letter is not in the secret word:
		* if it is a vowel: you lose two chances to guess the secret word
		* if it is a consonant: you only lose one chance to guess the secret word

* You are given 3 warnings:
	* if the letter is already guessed or a non alphabetical character, the game will warn you
	When you run out of warnings, you lose a chance to guess a letter

* Keep guessing letters until you correctly guess the secret word or you run out of chances to guess it
