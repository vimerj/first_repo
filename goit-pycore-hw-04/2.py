import re


def get_cats_info(path):
    cats = []
    path = "hw04_cats.txt"
    
    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    break
                cat_id, name, age = line.split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": int(age)
                }
                
                cats.append(cat)

    except FileNotFoundError:
        print("Файл не знайдено.")
    except ValueError:
        print("Помилка формату даних у файлі.")
    except Exception as e:
        print(f"Невідома помилка: {e}")

    return cats

cats_info = get_cats_info("hw04_cats.txt")
print(cats_info)
