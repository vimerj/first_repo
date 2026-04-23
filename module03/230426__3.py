from datetime import timezone, timedelta, datetime, date

# Get the current date and time
current_datetime = datetime.today()
print(current_datetime)

# Get the current date
current_date = date.today()
print(current_date)

from zoneinfo import ZoneInfo, available_timezones

print(datetime.now(timezone(timedelta(hours=2))))
#d.strftime (--> string format time) 
#strptime (--> string parse time)

user_date = "14/08/2010"
d = datetime.strptime(user_date, "%d/%m/%Y")
print(type(d))
print(d)

d1 = datetime.now()
d2 = datetime(2020, 1, 1)
print(d1 - d2)
