
def calculator_tip(bill,percentage,num_people):
    result = (bill / num_people) * percentage
    result = round(result, 2)
    result = "{:.2f}".format(result)

    print(f"Each person should py: ${result}")

def tip_calculator():
    bill = float(input("What was the total bill?\n"))
    percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
    percentage *= 0.01
    percentage += 1.0
    people_split = int(input("How many people to split the bill?\n"))
    calculator_tip(bill, percentage, people_split)

def run():
    print("Welcome to the tip calculator.")
    tip_calculator()


if __name__ == "__main__":
    run()