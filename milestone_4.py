import random

word_list = ["apple", "banana", "orange", "grape", "mango", 
          "pineapple", "strawberry", "blueberry", "kiwi", "peach"]

word = random.choice(word_list)
print(word)

def ask_for_input():
    while True:
        guess = input('Enter a letter: ')
        if len(guess) == 1 and guess.isalpha():
            break #exits the loop when a single letter is entered
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)    

def check_guess(guess):
    guess == guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')


class Hangman:
    def __init__ (self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = word
        self.word_guessed = ['_' for letter in self.word]  
        self.num_letters = len(set(self.word)) not in self.word_guessed
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess == guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')

    def ask_for_input(self):
        while True:
            guess = input('Enter a letter: ')
            if len(guess) != 1 or not guess.isalpha():
                 print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!') 
            else:
                check_guess(guess)
                self.list_of_guesses.append(guess)   
                print(self.word_guessed)   
                 

game1 = Hangman(word_list)
game1.ask_for_input()
