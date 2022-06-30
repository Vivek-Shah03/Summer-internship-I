import datetime as dt

# This can be done by using Date format codes
t = dt.datetime.now().strftime('%d %B %Y %H:%M %p %A')
print(t)
