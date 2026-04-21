customer = input("What is your name? >>>")
age = int(input("How old are you? >>>"))

if age > 18:
    message = f"Hello {customer}, welcome to the store! You are {age} years old."
    print(message)
elif age == 18:
    print("Congrats, enjoy your first beer!")
else:
    print("Not today, buddy.")