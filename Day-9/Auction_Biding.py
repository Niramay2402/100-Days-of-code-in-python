from art import logo
import os

print(logo)

bids = {}


def highest_bidder(bid_record):
    highest_bid = 0

    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with an amount of ${highest_bid}.")


answer = True
while answer:
    name = str(input("Enter your name:"))
    bid_placed = int(input("Enter the money placed: $"))

    bids[name] = bid_placed
    ans = input("Any more bets..? Type yes or no: ")
    if ans == 'no':
        answer = False
        highest_bidder(bids)
    elif ans == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
