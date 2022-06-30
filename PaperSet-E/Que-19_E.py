import datetime as dt
today = int(dt.date.today().day)
fom = dt.date.today() - dt.timedelta(today-1)
print(fom)
