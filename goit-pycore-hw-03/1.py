import datetime

def get_days_from_today(date):
    today = date.today()
    difference = today - date
    return difference.days

try:
    print(get_days_from_today(datetime.date(2010, 10, 33))) # тут вводіть дату в форматі рік, місяць, день
except Exception as e:
    print("An error occurred:", e)
    
print(get_days_from_today(datetime.date(2010, 10, 19))) # тут вводіть дату в форматі рік, місяць, день
