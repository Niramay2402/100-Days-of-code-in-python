from art import logo
import random

print(logo)
correct_ans = random.randint(1, 101)


print("Welcome to the Guessing Game!!! \nI'm thinking of a number between 1 to 100")
print(f"Correct Guess is {correct_ans}")
level = input("Choose difficulty level: 'hard' or 'easy': ")

if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5

if_guessed_right = 0

while not attempts == 0:
    print(f"You have {attempts} attempts remaining to guess the number")
    guessed_num = int(input("Guess a Number: "))

    if guessed_num == correct_ans:
        attempts = 0
        if_guessed_right = 1
        print(f"Guessed it right...The Answer was {correct_ans}.")
    elif guessed_num > correct_ans:
        attempts -= 1
        print("Too High")
    elif guessed_num < correct_ans:
        attempts -= 1
        print("Too Low")

if attempts == 0 and if_guessed_right != 1:
    print(f"You ran out of the attempts... You Lose. \nNumber to be Guessed was {correct_ans} ")