import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = area / cover
    result = math.ceil(num_of_cans)
    print(f"You'll need {result} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)