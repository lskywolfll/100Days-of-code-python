import random

def selecting_virtual_coin():
    random_state = random.randint(0, 1)

    if random_state == 1:
        return 'Heads'
    else:
        return 'Tails'

def run():
    random_coin = selecting_virtual_coin()
    print(random_coin)

if __name__ == "__main__":
    run()