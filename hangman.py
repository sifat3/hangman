import random
from words import words
import string


def get_valid_word(wor_d):
    word = random.choice(wor_d)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(wor_d)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letter) > 0 and lives > 0:
        # letter used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [i if i in used_letters else '-' for i in word]
        print('current word: ', ''.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

            else:
                lives = lives - 1  # takes away a life if wrong
                print('letter is not in word.')

        elif user_letter in used_letters:
            print("You have already used that character. Please try again")

        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 or when lives == 0

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')


hangman()
