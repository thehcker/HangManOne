# Project 2 Hangman

## HangMan part 1
This exercise is Part 1 of 3 of the Hangman exercise series. 
In this exercise, the task was to write a function that picks a random word from a list of words from the SOWPODS dictionary.This file was downloaded and saved in the same directory with the Python code.It is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. Each line in the file contains a single word.

<h3>What is SOWPODS</h3>
SOWPODS (currently known as Collins Scrabble Words) is a word list commonly used in word puzzles and games (like Scrabble for example).It is an anagram of the two acronyms OSPD (Official Scrabble Players Dictionary) and OSW (Official Scrabble Words), these being the original two official dictionaries used in various parts of the world at the time.

<strong>NB: Python random library was used for picking a random word.</strong>

The file has been saved in two formats(HTML and text format) and can therefore be read in either of the two formats in this project.

## HangMan part 2
This is Part 2 of 3 of the Hangman exercise series.
### Brief history of Hangman
In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).
### Instructions
Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.

An example interaction can look like this:
>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.


## Hangman part 3
This exercise is Part 3 of 3 of the Hangman exercise series. 
### Instructions
You can start your Python journey anywhere, but to finish this exercise you will have to have finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).
In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.
Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.

Optional additions:
When the player wins or loses, let them start a new game.
Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!
