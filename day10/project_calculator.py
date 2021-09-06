from art import logo
# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return n1 - n2

# Multiply


def multiply(n1, n2):
    return n1 * n2

# Divide


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)


    repeat_calculating = True
    last_value = 0

    while repeat_calculating:
        num1 = 0

        if last_value == 0:
            num1 = float(input("What's the first number?: "))
        else:
            num1 = last_value

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an opration from the line above: ")
        text_num2 = "What's the second number?: " if last_value == 0 else "What's the next number?: "
        num2 = float(input(text_num2))
        # First Method for have result
        # result = operations[operation_symbol](num1, num2)
        # Second Method
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        is_repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator operation, or type 'exit' to terminate calculating. : ")
        if is_repeat == 'y':
            last_value = answer
        elif is_repeat == 'exit':
            repeat_calculating = False
        else:
            repeat_calculating = False
            calculator()

calculator()