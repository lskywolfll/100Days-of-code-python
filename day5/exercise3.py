
def run():
    sum_even_numbers = 0

    for number in range(1, 101):
        if number % 2 == 0:
            sum_even_numbers += number
    
    print(f"Result sum with even numbers: {sum_even_numbers}")

if __name__ == "__main__":
    run()