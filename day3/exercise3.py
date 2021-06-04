
def run():

    bill = 0

    pizzas_bill = {
        "S": 15,
        "M":20,
        "L":25
    }

    pepperoni_bill = {
        "S": 2,
        "M": 3,
        "L": 3
    }

    extra_cheese_bill = 1

    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L : ")
    add_pepperoni = input("Do you want pepperoni? Y or N : ")
    extra_cheese = input("Do you want extra cheese? Y or N : ")

    if size == "S" or size == "M" or size == "L" and add_pepperoni == "Y" and extra_cheese == "Y":
        bill = pizzas_bill[size] + pepperoni_bill[size] + extra_cheese_bill
    elif size == "S" or size == "M" or size == "L" and add_pepperoni == "Y" and extra_cheese == "N":
        bill = pizzas_bill[size] + pepperoni_bill[size]
    elif size == "S" or size == "M" or size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
        bill = pizzas_bill[size] + extra_cheese_bill
    else:
        bill = pizzas_bill[size]

    print(f"Your final bill is {bill}")

if __name__ == "__main__":
    run()