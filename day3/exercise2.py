
#Problem
# Check if year it's Leap

def check_leap(year):
    division_4 = year % 4 == 0
    division_100 = year % 100 == 0
    division_400 = year % 400 == 0

    if division_4 and division_100 == False and division_400 == False:
        return True
    elif division_4 and division_100 == False and division_400:
        return True
    elif division_4 and division_100 and division_400:
        return True
    else:
        return False

def run():
    year_value = int(input("Which year do you want to check? "))
    is_leapyear = check_leap(year_value)

    if is_leapyear:
        print("Leap year.")
    else:
        print("Not leap year")

if __name__ == "__main__":
    run()