import random

word_list = ["apple", "banana", "orange", "grape", "mango", 
    "pineapple", "strawberry", "blueberry", "raspberry", 
    "watermelon", "peach", "cherry", "pear", "kiwi", 
    "plum", "pomegranate", "fig", "coconut", "lime", "lemon"]

word = random.choice(word_list)

guess = input('Enter a single letter: ')

if len(guess) == 1 and guess.isalpha() == True:
    print('Good guess!')
else:
    print('Oops! That is not a valid input')

# All good up to this point, no lag coming from input 