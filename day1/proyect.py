

def generator_name_band():
    country = input("What's name of the city you grew up in?\n")
    pet_name = input("What is the name of your pet?\n")

    band_name = f"{country} {pet_name}"

    return band_name

def run():
    
    print("Welcome to the Band Name Generator")
    band = generator_name_band()
    print(f"\nYour band name could be the {band}")

if __name__ == "__main__":
    run()