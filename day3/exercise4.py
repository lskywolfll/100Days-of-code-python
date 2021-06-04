
def love_scores(name1:str, name2:str):
    name = name1.lower() + name2.lower()
    total1 = 0
    total2 = 0

    occurs_T = name.count("t")
    occurs_R = name.count("r")
    occurs_U = name.count("u")
    occurs_E = name.count("e")

    total1 += occurs_T
    total1 += occurs_R
    total1 += occurs_U
    total1 += occurs_E

    occurs_L = name.count("l")
    occurs_O = name.count("o")
    occurs_V = name.count("v")
    occurs_E = name.count("e")

    total2 += occurs_L 
    total2 += occurs_O
    total2 += occurs_V
    total2 += occurs_E

    total = f"{total1}{total2}"
    total = int(total)

    return total

def run():
    print("Welcome to the Love Calculator")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
    love_score = love_scores(name1, name2)
    print(f"love_score: {love_score}")

    if love_score < 10 or love_score > 90:
        print(f"Your score is {love_score}, you go together like coke and mentos.")
    elif love_score >= 40 and love_score <= 50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"Your score is {love_score}.")

if __name__ == '__main__':
    run()