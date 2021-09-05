from art import logo
from os import system


def clear_console():
    system('clear')


def find_highest_bidder(bidding_record: dict):
    highest_bid = 0
    winner = ""

    for name,price in bidding_record.items():
        if highest_bid < price:
            highest_bid = price
            winner = name

    print(f"The winner is {winner} with a bid of ${highest_bid}.") 


print(logo)

bids = {}

bidding_finished = False

while not bidding_finished:
    name = input('What is your name?: ')
    price = int(input("What's your bid?: "))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no': ")
    if should_continue == 'yes':
        clear_console()
    else:
        clear_console()
        find_highest_bidder(bids)
        bidding_finished = True
