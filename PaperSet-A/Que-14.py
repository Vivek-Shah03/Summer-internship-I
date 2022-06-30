from datetime import date

date1 = date(2022, 1, 1)
date2 = date(2022, 2, 22)
day_diff = (date2-date1).days
print(f"Number Of Days: {day_diff}")
