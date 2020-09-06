import sys
import random

"""
A short command line Python program that has the
user attempt to guess a random number
"""

num = random.randint(1, 10)
print("\nI'm thinking of a number between 1 and 10. You have 5 attempts to guess the correct number!")

for i in range(5):
    user_guess = int(input(f'\nGuess a number!                             Guesses remaining: {5-i}\n'))
    if user_guess == num:
        print(f'Congatulations!\nI was thinking of the number {num}\nIt took you {i+1} guesses')
        sys.exit()
    elif user_guess < num:
        print(f'{user_guess} is too low')
    else:
        print(f'{user_guess} is too high')
print(f"\nI'm sorry, you've ran out of guesses.\nThe number I was thinking of was: {num}")
sys.exit()
        