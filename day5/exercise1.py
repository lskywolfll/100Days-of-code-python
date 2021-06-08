import math

def run():
    student_heights = [156, 178, 165, 171, 187]
    total_heights = 0

    for height_student in student_heights:
        total_heights += height_student
    
    total_heights /= len(student_heights)
    total_heights = round(total_heights)

    print(total_heights)


if __name__ == "__main__":
    run()