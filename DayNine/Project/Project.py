from os import system, name
from art import logo

bids = {}

print(logo)


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def add_bid(bidder_name, bid):
    bids[bidder_name] = bid
    return


def enter_bid():
    bidder_name = input('Enter your name: ')
    print('Hello, ' + bidder_name + '!')
    bid = input('Enter your bid: $')
    print('\nThank you for your bid of $' + bid + '!')
    add_bid(bidder_name=bidder_name, bid=bid)
    return


def ask_bid():
    bid_again = True
    while bid_again:
        print("Are there any other bids? (y/n)")
        answer = input()
        if answer == 'y':
            clear()
            enter_bid()
        else:
            bid_again = False
    return


def calculate_winner(bid_record):
    highest_bid = 0
    winner = ''
    for bidder_name, bid in bid_record.items():
        if int(bid) > highest_bid:
            highest_bid = int(bid)
            winner = bidder_name
    return winner, highest_bid


def win_bid(winner, bid_amount):
    print(f"The winner is {winner} with a bid of ${bid_amount}!")
    return


def main():
    print('Welcome to the secret Auction House!')
    enter_bid()
    ask_bid()
    clear()
    winner, highest_bid = calculate_winner(bids)
    win_bid(winner=winner, bid_amount=highest_bid)


if __name__ == '__main__':
    main()
