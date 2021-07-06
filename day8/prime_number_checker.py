
def check_prime_number(number):
    # First Method
    # divisors = 0

    # for i in range(2, number + 1):
    #     residuo = number % i

    #     if number % i == 0:
    #         print("not prime")

    #     if residuo == 0:
    #         divisors += 1
    
    # is_prime = True if divisors == 2 else False
    # Second Method
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    return is_prime

def run():
    number = int(input("Check this numero: "))
    is_prime = check_prime_number(number)
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not prime number.")
    
if __name__ == "__main__":
    run()