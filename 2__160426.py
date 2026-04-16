numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        numbers.append(int(user_input))
    except ValueError:
        print("Please enter a valid number.")

print(f"Amount of numbers: {len(numbers)}")
print(f"Numbers: {numbers}")
