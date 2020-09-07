import requests, sys

# setup, get random word from api
x = requests.get('https://random-word-api.herokuapp.com/word?number=1').json()
word = list(x[0].lower())
user_word = ['*' for letter in word]
guesses = []
lives = max(min(len(word), 10), 3)


# main loop
def main():
    while lives > 0:
        print(f'\nWord: {"".join(user_word)}            lives: {lives}          Guesses: {guesses}')

        # check if user has won
        if word == user_word:
            print('Congratulations, you won!')
            sys.exit()

        guess = user_guess()
        check_guess(guess)

    print(f'Sorry, you ran out of lives! The word was {"".join(word)}')
            

# takes a valid keyboard input from the user
def user_guess():
    while True:
        letter = input('Guess a letter\n').lower()
        if len(letter) != 1 or not letter.isalpha():
            print('invalid input\n')
            continue
        else:
            return(letter)


# checks if user's guess exists in word. Reveals correctly guessed letters in word.
# Subtracts life if guess not in word
def check_guess(guess):
    global lives

    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                user_word[i] = guess
    else:
        lives -= 1

    guesses.append(guess)


if __name__ == "__main__":
    main()