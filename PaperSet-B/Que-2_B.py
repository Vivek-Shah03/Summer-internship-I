import datetime


day = int(input("Enter Day: "))
month = int(input("Enter Month: "))
year = int(input("Enter Year: "))

local = datetime.datetime(year, month, day)
local = local.utcnow()
print(local)