from art import logo
import random

print(logo)
correct_ans = random.randint(1, 101)

print("Welcome to the Guessing Game!!! \nI'm thinking of a number between 1 to 100")
# print(f"Correct Guess is {correct_ans}")
level = input("Choose difficulty level: 'hard' or 'easy': ")

if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5

# a variable that would help avoid printing losing statements
# when we guess the correct number and get out of the loop
if_guessed_right = False

while not attempts == 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guessed_num = int(input("Guess a Number: "))

    if guessed_num == correct_ans:
        attempts = 0  # To get out of the While Loop
        if_guessed_right = True  # To avoid printing the Losing statement
        print(f"Guessed it right...The Answer was {correct_ans}.")
    elif guessed_num > correct_ans:
        attempts -= 1
        print("Too High")
    elif guessed_num < correct_ans:
        attempts -= 1
        print("Too Low")

if attempts == 0 and if_guessed_right is False:
    print(f"You ran out of the attempts... You Lose. \nNumber to be Guessed was {correct_ans} ")
