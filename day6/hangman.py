
import random
import os
import unidecode

# Objetive
words = []
# Player
actual_words = []
lives = 7


def generated_random_word():
    with open('./data.txt', 'r') as f:
        words = [x.strip() for x in f.readlines()]
        return random.choice(words)


def clear_console():
    os.system('clear')


def generated_blank_spaces(phrase):
    status = ""
    SPACES = " _ "

    for i in range(0, len(phrase)):
        if i >= len(actual_words):
            status += SPACES
            continue
        elif actual_words[i] == phrase[i]:
            status += f" {actual_words[i].upper()} "
        else:
            status += SPACES

    print(status + '\n')


def get_input():
    while True:
        value = input("Escoge una letra: ")
        if len(value) > 1:
            raise ValueError("No se admite mas de una letra")
        elif len(value) == 0:
            raise ValueError(
                "Por favor ingresar una letra, no se admiten textos vacios")
        elif value == "":
            raise ValueError("No se admiten textos vacios")

        return value.lower()


def validate_character(new_char, objetive):
    e_listwords = enumerate(objetive)

    for index, character in e_listwords:
        if character.lower() == new_char.lower():
            actual_words[index] = new_char
            return True

    return False


def game(phrase):
    # clear_console()
    global lives
    list_phrase = []
    for char in phrase:
        list_phrase.append(char)
        actual_words.append("")

    while actual_words != list_phrase:
        print(f"lives: {lives}")
        generated_blank_spaces(phrase)
        new_phrase = get_input()
        check = validate_character(new_phrase, phrase)
        
        if check == False:
            lives -= 1
        
        if lives == 0:
            break
        



    if lives > 0 and actual_words == list_phrase:
        print("Win")
    elif lives == 0:
        print(f"Lose word is: {phrase}")


def run():
    word = generated_random_word()
    game(word)


if __name__ == "__main__":
    run()
