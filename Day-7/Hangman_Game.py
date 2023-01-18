import random

from hangman_art import stages, logo

from hangman_wordlist import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    
    if guess in display:
        print("You already have guessed this letter")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
   
   #Check for lives
    if guess not in chosen_word:
        print(f"You guessed the letter {guess}, which is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You Lose")
            print(f"The word was {chosen_word}.")
            end_of_game = True

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        print("")

    print(stages[lives])