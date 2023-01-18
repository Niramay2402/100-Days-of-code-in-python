#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display=[]
guess=""
LenOfWord = (len(chosen_word))

for LenOfWord in chosen_word:
  display.append("_")

print(display)
#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word
# and 'display' has no more blanks ("_"). Then you can tell the user they've won.
print("")
end = False

while not end:
    print("")
    guess = input("Guess a letter: ").lower()
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    print(f"{' '.join(display)}")
            
    if "_" not in display:
        print("")
        print("You Win")
        end = True