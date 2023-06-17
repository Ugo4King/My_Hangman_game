# Hangman Game
## Milestone One

- Create a pythone fine.
- create a variable in the python file that takes a list of five fruites.
- import a random and randomely select from the list of five fruites
- ask the user to guess a letter and assign the letter to a variable called guess
- write and if statement that will check if the legnth od the input provided by the user is 1 and also an alphabet.
- print "good guess" if the conditions are met
- print thats wrong if the conditions are not met

## Defining a function
- check_guess function was created and the code that checked if the guessed letter is in the word that was randomely selected from the list of fruites.
- ask_for_input function was created and the code that asked for the user to guess a letter was included under the function and an if statement that checked if the guessed letter is a single word and an alphabetet was also included under the function.
## Define a class
- A Class was created which innitialized word_list, num_lives, list_of_guesses etc. 
- The check_guess ask_for_input methods were also created under the class.
- The ask_for_input method contains a while loop, and if statements that checked if the letter guessed is not a single letter and as well if it is not an alphabate and print invalid letter if the conditions are met.
- it checks if the letter has been guessed before and print you have used the letter befor it has ben guessed before.
- it adds to the list_of_guesses after every correct guess
- it also called the check_guess method under it and printed you win before bracking out of the loop.
- the check_guess checked if the guessed word is in the randomely selected word and printed good guess if it correct and used a for loop to iterate over the length of the selected word.
- if the guessed letter is correct it addes it the the list of word guessed by using an if statement to check that the guessed letter is in the word.
