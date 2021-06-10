
def word_fizz_buzz(number):
    fizz = 3
    buzz = 5

    if number % fizz == 0 and number % buzz == 0:
        print("FizzBuzz")
    elif number % fizz == 0:
        print("Fizz")
    elif number % buzz == 0:
        print("Buzz")
    else:
        print(number)

def run():
    max_numbers = 100

    for number in range(1, max_numbers + 1):
        word_fizz_buzz(number)

if __name__ == '__main__':
    run()