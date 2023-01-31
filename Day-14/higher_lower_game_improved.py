from art import logo, vs
from game_data import data
from os import system, name
import random

# Display art
print(logo)
score = 0
game_over = False
random_B = random.choice(data)


# Clears the terminal
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Make game repeatable
while not game_over:
    # Make account at position B become the next account at position A
    # Generate a random  account from the game account list
    random_A = random_B
    random_B = random.choice(data)

    # check if account A is the same as account B
    while random_A == random_B:
        random_B = random.choice(data)

    # Format the account data into a printable format
    def format_data(account):
        account_name = account["name"]
        account_desc = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_desc}, from {account_country}"

    # Compare followers count
    def check_ans(choice, a_followers, b_followers):
        """Take the user guess and follower counts, return True or False"""
        if a_followers > b_followers:
            return choice == "a"
        else:
            return choice == "b"

    print("Compare A: " + format_data(random_A))
    print(vs)
    print("Against B: " + format_data(random_B))

    # Ask user for a guess

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    # get follower count of each account
    A_follower_count = random_A["follower_count"]
    B_follower_count = random_B["follower_count"]

    is_correct = check_ans(guess, A_follower_count, B_follower_count)
    clear()
    print(logo)

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
