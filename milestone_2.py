import random 

word_list = ['Banana', 'Mango', 'Orange', 'Plantain', 'Avacado-Pear']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a singl letter ")

if len(guess) == 1 and guess.isalpha():
    print("Good Guess!")
else:
    print("Oops! That is not a valid input")
