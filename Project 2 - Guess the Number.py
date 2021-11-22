"""
Project 2 - GUESS THE NUMBER (COMPUTER)
Apply the function
Use the RANDOM lib - https://docs.python.org/3/library/random.html
"""

import random
def guess(x):
    random_number = random.randint(1, x) #Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
    """ Use while loop to guess and stop when we guess the right number"""
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Too low')
        elif guess > random_number:
            print('Too high')
    print(F'CONGGRAT!!!. {random_number} IS THE RIGHT NUMBER')

guess(10)
