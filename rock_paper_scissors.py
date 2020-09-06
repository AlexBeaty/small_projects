import sys
import random

"""
The user plays rock, paper, scissors against the computer in the command line
"""

hands = {
    1:'rock',
    2:'paper',
    3:'scissors'
}

outcomes = {
    'rockrock': 0,
    'rockpaper': -1,
    'rockscissors': 1,
    'paperpaper': 0,
    'paperrock': 1,
    'paperscissors': -1,
    'scissorsscissors': 0,
    'scissorspaper': 1,
    'scissorsrock': -1
}

print('\nLet\'s play Rock, Paper, Scissors!\n')

while True:
    c_hand = hands[random.randint(1,3)]
    p_hand = input('Type the name of the hand your playing...(e.g. \'rock\')')

    if p_hand not in hands.values():
        print('Sorry, that isn\'t a valid hand, try again')
        continue

    outcome = outcomes[p_hand+c_hand]
    print(f'You: {p_hand}, Comp: {c_hand}')

    if outcome == 0:
        print('Tie! Play again')
    elif outcome == -1:
        print('Sorry, you lost')
        break
    elif outcome == 1:
        print('Congratulations, you won!')
        break
    else:
        print('The game broke')
