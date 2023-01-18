import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_move = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors. "))
print("")
print("You Chose:")

if user_move == 0:
    print(rock)
elif user_move == 1:
    print(paper)
elif user_move == 2:
    print(scissors)
else:
    print("Enter A Valid Character ")


computer_move = random.randint(0,2)

print("")
print("Computer Chose:")

if computer_move == 0:
    print(rock)
elif computer_move == 1:
    print(paper)
elif computer_move ==2:
    print(scissors)
else:
    print("Enter a Valid character")


if user_move == 2 and computer_move == 0:
    print("You Lose")
elif computer_move == 0 and user_move ==0:
    print("You Win")
elif user_move == computer_move:
    print("Its a tie")
elif computer_move > user_move:
    print("You lose")
elif computer_move < user_move:
    print("You Win!!")
else:
    print("Entered a invalid character")
    
