import random

word_list = ["apple", "banana", "orange", "grape", "mango", 
    "pineapple", "strawberry", "blueberry", "raspberry", 
    "watermelon", "peach", "cherry", "pear", "kiwi", 
    "plum", "pomegranate", "fig", "coconut", "lime", "lemon"]

word = random.choice(word_list)
print(word)

class Hangman:
    word = random.choice(word_list)
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = ['_' for letter in word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in word:
            print(f'Good guess! "{guess}" is in the word.')
            for idx,letter in enumerate(self.word):
                if letter == word:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, "{guess}" is not in the word.')
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input('Enter a single letter: ')
            if len(guess) != 1 or guess.isalpha() == False:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print( "You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

game1 = Hangman(word_list) 

game1.ask_for_input()
