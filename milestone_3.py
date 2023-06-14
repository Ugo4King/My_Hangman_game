
import random 
# # Create a list of five fruites
# word_list = ['Banana', 'Mango', 'Orange', 'Plantain', 'Avacado-Pear']
# # randomly select from the list of five fruites and make it your magic word

# word = random.choice(word_list)

# while True:
#     guess = input("Enter a single Letter ")
#     if guess.isalpha():
#         break
#     else:
#         print("Invalid letter. Please, enter a single alphabetical character.")
# if guess in word:
#     print(f"Good guess! {guess} is in the word.")
# else:
#     print(f"Sorry, {guess} is not in the word. Try again.")
word_list = ['Banana', 'Mango', 'Orange', 'Plantain', 'Avacado-Pear']
word = random.choice(word_list)


def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False 


def ask_for_input():        
    while True:
        guess = input("Enter a single Letter ")
        if guess !=1 and not guess.isalpha():
            print("Try a single letter")
    
        else:
            if check_guess(guess):
                break
            
ask_for_input()

