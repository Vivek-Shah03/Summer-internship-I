import datetime


def ageCalculator(c_year, c_month, c_day, b_year, b_month, b_date):
    import datetime
    today = datetime.date(c_year, c_month, c_day)
    dob = datetime.date(b_year, b_month, b_date)
    c_year= ((today - dob).total_seconds() / (365.242 * 24 * 3600))
    yearsInt=int(c_year)
    c_month= (c_year - yearsInt) * 12
    monthsInt=int(c_month)
    c_day= (c_month - monthsInt) * (365.242 / 12)
    daysInt=int(c_day)
    print('You are {0} year, {1} month, {2} day old.'.format(yearsInt,monthsInt,daysInt))

b_year = int(input("Enter Birthday Year: "))
b_month = int(input("Enter Birthday Month: "))
b_day = int(input("Enter Birthday Day: "))
c_year = datetime.datetime.today().year
c_month = datetime.datetime.today().month
c_day = datetime.datetime.today().day
ageCalculator(c_year, c_month, c_day, b_year, b_month, b_day)
