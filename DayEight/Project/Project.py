#!/usr/bin/env python3
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)


def play():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("\nEnter a message: ")
    shift = int(input("\nEnter a shift: "))
    encrypt_decrypt(message, shift, direction)

    # if direction == "encode":
    #     encrypt(message, shift)
    # elif direction == "decode":
    #     decrypt(message, shift)
    # return


def encrypt_decrypt(message, shift, action):
    text = ""
    if action == "decode":
        shift *= -1
    for char in message:
        if char.isalpha():
            position = alphabet.index(char)
            new_position = (position + shift) % 26
            new_letter = alphabet[new_position]
            text += new_letter
        else:
            text += char
    print(f"The {action}d text is {text}")


def main():
    go_again = True
    while go_again:
        play()
        go_again = input("\nWould you like to go again? (y/n): ")
        while go_again != "y" and go_again != "n":
            go_again = input("\nWould you like to go again? (y/n): ")
        if go_again == "n":
            go_again = False
            print("\nThanks for playing!")
        print("\n")
    print("Goodbye!")


if __name__ == "__main__":
    main()


# def encrypt(message, shift):
#     cypher_text = ""
#     for letter in message:
#         position = alphabet_index = alphabet.index(letter)
#         new_position = (position + shift) % 26
#         new_letter = alphabet[new_position]
#         cypher_text += new_letter
#     print(f"The encoded text is {cypher_text}")


# def decrypt(message, shift):
#     decrypted_text = ""
#     for letter in message:
#         position = alphabet_index = alphabet.index(letter)
#         new_position = (position - shift) % 26
#         new_letter = alphabet[new_position]
#         decrypted_text += new_letter
#     print(f"The decrypted text is {decrypted_text}")
