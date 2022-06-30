import datetime as dt
today = dt.datetime.today()
after_month = (today + dt.timedelta(days=30)).date()
print(after_month)