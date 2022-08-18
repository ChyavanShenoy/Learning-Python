import random
from words import word_list
import asciiart
from os import system, name
guess_list = []
selected_word = ""


# Input the guess letter


def get_guess():
    guess = input("Guess a letter: ").lower()
    return guess


# Sets the default guess list to the length of the selected word and replaces with "_"
def set_guess_default(selected_word_length):
    for _ in range(selected_word_length):
        guess_list.append("_")


# Selects a random word from the word_list
def select_word():
    choice = random.choice(word_list)
    return choice, len(choice)


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    print(asciiart.logo)
    selected_word, selected_word_length = select_word()
    player_lives = 6
    set_guess_default(selected_word_length)
    end_of_game = False
    while not end_of_game:
        entered_alphabet = get_guess()
        clear_screen()
        if entered_alphabet in guess_list:
            print("You already guessed that letter")
        else:
            for position in range(selected_word_length):
                letter = selected_word[position]
                if entered_alphabet == letter:
                    guess_list[position] = letter
            if entered_alphabet not in selected_word:
                print("You guessed wrong, try again")
                player_lives -= 1
                if player_lives == 0:
                    print("\nYou lose")
                    end_of_game = True
            print(asciiart.stages[player_lives])
            print(" ".join(guess_list))

        if "_" not in guess_list:
            print("You win!")
            end_of_game = True


if __name__ == "__main__":
    main()
