from game_data import data
from art import logo, vs
import random

# print(data)
print(logo)

player1 = random.choice(data)
player2 = random.choice(data)

print(f"Compare A: {player1['name']} , a {player1['description']} from {player1['country']}.")
print(vs)
print(f"Against B: {player2['name']} , a {player2['description']} from {player2['country']}.")
print("\n")
P1 = (player1['follower_count'])
P2 = (player2['follower_count'])


# def compare_players(player1, player2):
#
#     if player1["follower_count"] > player2["follower_count"]:
#         return player1["name"]
#     elif player1["follower_count"] < player2["follower_count"]:
#         return player2["name"]
#     else:
#         return "It's a tie!"

score = 0
right_choice = True

while right_choice:

    its_correct = True
    if its_correct == True:
        decide = input("Who has more followers? Type '1' for Player 1 and '2' for player 2: ")
        print(vs)

    if decide == "1":
        if P1 > P2:
            score += 1
            print(f"You are right. Your current score is {score}.")
            player1 = random.choice(data)
            print(f"Compare A: {player1['name']} , a {player1['description']} from {player1['country']}.")
        elif P1 < P2:
            its_correct = False
            right_choice = False
            print(f"Its Wrong . Your Final Score is {score}.")
        else:
            print("It's a tie")
    elif decide == "2":
        if P1 > P2:
            its_correct = False
            right_choice = False
            print(f"Its Wrong . Your Final Score is {score}.")
        elif P1 < P2:
            score += 1
            print(f"You are right. Your current score is {score}.")
            player2 = random.choice(data)
            print(f"Against B: {player2['name']} , a {player2['description']} from {player2['country']}.")
        else:
            print("It's a tie")
    else:
        print("Invalid input")
        right_choice = False

print(f"{player1['name']} is {player1['follower_count']} and {player2['name']} is {player2['follower_count']}")