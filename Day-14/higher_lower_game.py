from game_data import data
from art import logo, vs
import random

# print(data)
print(logo)

player1 = random.choice(data)
player2 = random.choice(data)

print(f"Compare A: {player1['name']} , a {player1['description']} from {player1['country']}.")
print(f"Compare B: {player2['name']} , a {player2['description']} from {player2['country']}.")
print("\n")
P1 = (player1['follower_count'])
P2 = (player2['follower_count'])


def compare_players(player1, player2):

    if player1["follower_count"] > player2["follower_count"]:
        return player1["name"]
    elif player1["follower_count"] < player2["follower_count"]:
        return player2["name"]
    else:
        return "It's a tie!"


right_choice = True

while right_choice:

    decide = input("Who has more followers? Type '1' for Player 1 and 'p2' for player 2: ")
    print(vs)

    if decide == "1":
        if P1 > P2:
            print(f"{player1['name']} has more followers")
        elif P1 < P2:
            right_choice = False
            print(f"{player2['name']} has more followers")
        else:
            print("It's a tie")
    elif decide == "2":
        if P1 > P2:
            print(f"{player2['name']} has more followers")
        elif P1 < P2:
            right_choice = False
            print(f"{player1['name']} has more followers")
        else:
            print("It's a tie")
    else:
        print("Invalid input")
        right_choice = False

print(f"{player1['name']} is {player1['follower_count']} and {player2['name']} is {player2['follower_count']}")