

def run():
    age = int(input("What is your current age?\n"))
    years_remaining = 90 - age
    days_remaining = years_remaining * 365
    weeks_remaining = years_remaining * 52
    months_remaining = years_remaining * 12

    message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"
    print(message)

if __name__ == '__main__':
    run()