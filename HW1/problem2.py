import datetime
import time
import calendar

bd = datetime.date(year = 1998, month = 6, day = 4)
now = datetime.date.today()
yesterday = now-datetime.timedelta(days=1)
this_bd = datetime.date(year = now.year, month = bd.month, day = bd.day)
next_bd = datetime.date(year = now.year+1, month = bd.month, day = bd.day)

print(bd)
print(bd.year)
print(calendar.month_name[bd.month])
print(bd.day)
print(calendar.day_name[bd.weekday()])

if this_bd>now:
    print((this_bd-now).days)
else:
    print((next_bd-now).days)

print(calendar.month(2017, 5))
print(yesterday)
print(yesterday+datetime.timedelta(days=2))
print(yesterday-datetime.timedelta(days=3))

