# blackjack rules:
#   - cards 2-10 are worth their face value
#   - Jack, Queen, King are worth 10
#   - Ace is worth 1 or 11
#   - player and dealer start with 2 cards
#   - player can see one of the dealer's cards
#   - player can ask for another card (hit) or stop (stand)
#   - player can hit as many times as they want
#   - if player goes over 21, they bust and lose
#   - dealer must hit until they reach 17
#   - if dealer goes over 21, they bust and player wins
#   - if player and dealer both under 21, highest score wins
#   - if player and dealer have same score, it's a draw

import random
from art import logo

list_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10 ,10, 10]

