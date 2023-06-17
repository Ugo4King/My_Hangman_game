import milestone_4

# create a function
def play_game(self, word_list):
    self.num_lives = 5
    game = Hangman(self.word_list, self.num_lives)
    while True:
        if self.num_lives == 0:
            print("You Lost")
        elif self.num_lives != 0 and num_letters > 0:
            print("Congratulation You Wine!")
play_game(word_list)



