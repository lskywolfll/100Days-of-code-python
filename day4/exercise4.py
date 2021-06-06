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

games_images = [rock, paper, scissors]

def winner_choose(human, computer):

    is_winner = False
    is_tie = False

    if human >= 3 or human < 0:
        print("You typed an invaid number, you lose!")
    else:
        if human == 0 and computer == 2:
            is_winner = True
        elif computer == 0 and human == 2:
            is_winner = False
        elif computer > human:
            is_winner = False
        elif human > computer:
            is_winner = True
        elif human == computer:
            is_tie = True

        if is_tie:
            print("It's a draw")
        elif is_winner:
            print("You win")
        else:
            print("You lose")

def run():
    choose = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    choose_random = random.randint(0, 2)
    print("\n")
    print(games_images[choose])
    print(f"\nComputer chose:\n{games_images[choose_random]}")
    winner_choose(choose, choose_random)

if __name__ == "__main__":
    run()