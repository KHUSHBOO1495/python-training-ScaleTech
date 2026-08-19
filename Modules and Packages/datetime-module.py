from datetime import datetime, timedelta
from datetime import date

print(datetime.now())
print(date.today())
print(date(2000, 5, 15))

today = date.today()
print(today.year)
print(today.month)
print(today.day)

now = datetime.now()
print(now.hour)
print(now.minute)
print(now.second)

formatted = now.strftime("%d-%m-%Y")
print(formatted)

# %Y → 2026
# %m → 08
# %d → 18
# %H → hour (24-hour)
# %M → minute
# %S → second

print(now.strftime("%Y-%m-%d %H:%M:%S"))

date_string = "18-08-2026"
date_object = datetime.strptime(date_string, "%d-%m-%Y")

today = datetime.now()
tomorrow = today + timedelta(days=1)
print(tomorrow)

start = date(2005, 9, 14)
end = date(2026, 8, 19)
difference = end - start
print(difference.days // 365)

