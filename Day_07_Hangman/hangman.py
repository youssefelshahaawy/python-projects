import random
import sys

from stages import*
from word_list import*

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while "_" in display:    
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")
        

#Check guessed letter 
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)
        
    if guess not in chosen_word:
        print("Letter is not in the word\nYou lost a life")
        lives -= 1
        print(stages[lives])
        print(display)
        if lives == 0:
            print("you lose")
            sys.exit (0)
        

print("You win !")
print(display)