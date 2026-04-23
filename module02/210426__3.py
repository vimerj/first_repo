print("=== Dragon Game ===")

while True:
    print("1 - Start a new game")
    print("2 - Load a saved game")
    print("3 - Settings")
    print("4 - Quit")
    choice = input("Enter your choice: ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select a valid option.")
        continue

    if choice == '1':
        print("Starting a new game...")
    elif choice == '2':
        print("Loading a saved game...")
    elif choice == '3':
        print("Opening settings...")
    elif choice == '4':
        print("Quitting the game...")
        break