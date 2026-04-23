import random

def generate_car_plate():
    set_of_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    set_of_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    p1 = "BH"
    p2 = ""
    for i in range(4):
        p2 += str(random.choice(set_of_digits))
    p3 = ""
    for i in range(2):
        p3 += str(random.choice(set_of_letters))
    print(p1 + " " + str(p2) + " " + p3)

for i in range(10):
    generate_car_plate()