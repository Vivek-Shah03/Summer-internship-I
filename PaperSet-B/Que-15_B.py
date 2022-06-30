import datetime as dt
import calendar


def last_day_of_month(date):
    return calendar._monthlen(date.year, date.month)


month_last_day = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                  9: "September", 10: "October", 11: "November", 12: "December"}
first_day = 1
month = dt.datetime.today().month
year = dt.datetime.today().year
fd = dt.datetime(year, month, first_day)
day_number = dt.datetime.weekday(fd)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
name_of_day = days[fd.weekday()]
last_day = last_day_of_month(fd)
ld = dt.datetime(year, month, int(last_day))
name_of_last_day = days[dt.datetime.weekday(ld)]
month = month_last_day[month]
print(f"{first_day}st {month} {year} {name_of_day} {dt.datetime.time(fd)} AM")
print(f"{last_day_of_month(fd)}st {month} {year} {name_of_last_day} {dt.datetime.time(fd)} PM")
