

def calculate_ibm(height, weight):

    result = weight / (height ** 2)
    result = int(result)

    return result

def run():
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    ibm = calculate_ibm(float(height), int(weight))
    print(ibm)

if __name__ == '__main__':
    run()