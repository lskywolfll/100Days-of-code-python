

def status_bmi(bmi):
    if bmi < 18.5:
        print("Estas Bajo Peso")
    elif bmi > 18.5 and bmi < 25:
        print("Tienes Peso Normal")
    elif bmi > 25 and bmi < 30:
        print("Estas Sobre Peso")
    else:
        print("Tienes Obesidad")

def calculate_bmi(height, weight):

    result = weight / (height ** 2)
    status_bmi(result)
    result = int(result)

    return result

def run():
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    bmi = calculate_bmi(float(height), int(weight))
    print(bmi)

if __name__ == '__main__':
    run()