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

dict_choosers = {
    "0":rock,
    "1": paper,
    "2": scissors
}

def winner_choose(human, computer):

    is_winner = False
    is_tie = False

    if computer == 2 and human == 1:
        is_winner = False
    elif computer == 2 and human == 0:
        is_winner = True
    elif computer == 2 and human == 2:
        is_tie = True
    elif computer == 1 and human == 1:
        is_tie = True
    elif computer == 1 and human == 2:
        is_winner = True
    elif computer == 1 and human == 0:
        is_winner = False
    elif computer == 0 and human == 0:
        is_tie = True
    elif computer == 0 and human == 1:
        is_winner = True
    elif computer == 0 and human == 2:
        is_winner = False

    if is_tie:
        print("Tie")
    elif is_winner:
        print("You win")
    else:
        print("You lose")

def run():
    choose = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    choose_random = random.randint(0, 2)
    print("\n")
    print(dict_choosers[str(choose)])
    print(f"\nComputer chose:\n{dict_choosers[str(choose_random)]}")
    winner_choose(choose, choose_random)




if __name__ == "__main__":
    run()