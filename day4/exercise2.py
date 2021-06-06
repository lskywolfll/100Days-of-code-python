import random

def run():
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    
    pay_bill = random.choice(names)
    print(f"{pay_bill} is going to buy the meal today!")

if __name__ == '__main__':
    run()