import random
import os
from hangman_art import stages, logo
from hangman_words import word_list

def clear():
    os.system('clear')

print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Adivina la letra: ").lower()

    clear()

    if guess in display:
        print(f"Tú ya has adivinado la letra '{guess}'")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"\n{' '.join(display)}")

    if guess not in chosen_word:
        print(f"Tu escogiste '{guess}', eso no esta en la palabra. tu pierdes una vida.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("Tu pierdes.")
    
    if not "_" in display:
        game_is_finished = True
        print("Tu ganas.")

    print(stages[lives])