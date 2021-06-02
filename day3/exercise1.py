
#Problem
# detec even number

def is_even_number(number):
    if number % 2 == 0:
        return True
    else:
        return False

def run():
    number = int(input("Which number do you want to check? "))
    result = is_even_number(number)

    if result:
        print("This is an even number!")
    else:
        print("This is an odd number!")

if __name__ == "__main__":
    run()