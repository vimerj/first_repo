from typing import Callable
from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Ім'я не може бути порожнім")
        super().__init__(value)
		

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError(f"Номер телефону має містити рівно 10 цифр, отримано: {value}")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            # Перевіряємо формат DD.MM.YYYY
            datetime.strptime(value, "%d.%m.%Y")
            self.value = value
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Телефон {old_phone} не знайдено")
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return self.data

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Запис з ім'ям {name} не знайдено")
    
    def get_upcoming_birthdays(users):
        today = datetime.today().date()
        result = []

        for user in users:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= 7:
                congratulation_date = birthday_this_year

                if congratulation_date.weekday() == 5: # субота
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:  # неділя
                    congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

        return result
    

def input_error(func: Callable):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please." if func.__name__ in ["add_contact", "change_contact"] else "Enter user name"
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"Error: {str(e)}"
    return inner


@input_error
def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change <name> <phone>"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone <name>"
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) != 2:
        return "Usage: add-birthday [name] [DD.MM.YYYY]"
    name, date_str = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_birthday(date_str)
    return f"Birthday added for {name}."


@input_error
def show_birthday(args, book: AddressBook):
    if not args:
        return "Usage: show-birthday [name]"
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact not found."
    if not record.birthday:
        return f"{name} has no birthday saved."
    return f"{name}'s birthday: {record.birthday.value}"


@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next 7 days."
    result = "Upcoming birthdays:\n"
    for item in upcoming:
        result += f"{item['name']}: {item['congratulation_date']}\n"
    return result.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))
        
        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону в записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
book.delete("Jane")


if __name__ == "__main__":
    main()