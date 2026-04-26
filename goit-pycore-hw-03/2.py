import random

def get_numbers_ticket(min, max, quantity):
    try:
        print(get_numbers_ticket)
        if min <= 0:
            print("Мінімальне число повинно бути більше 0.")
        elif max > 1000:
            print("Максимальне число не повинно бути більше 1000.")
        elif quantity <= 0:
            print("Кількість чисел повинна бути більше 0.")
        elif min >= max:
            print("Мінімальне число повинно бути менше максимального.")
        elif quantity >= max:
            print("Кількість чисел повинна бути менше максимального числа.")
        else:
            pass
    except ValueError:
        print("Будь ласка, введіть коректні числа.")
    
    numbers = set()
    while len(numbers) < quantity:
        number = random.randint(min, max)
        numbers.add(number)
    return sorted(numbers)
    
try:
    min = int(input("Введіть мінімальне число: "))
    max = int(input("Введіть максимальне число: "))
    quantity = int(input("Введіть кількість чисел: "))
    
    result = get_numbers_ticket(min, max, quantity)
    print("Ваші числа:", result)

except ValueError as e:
    print("Помилка:", e)
