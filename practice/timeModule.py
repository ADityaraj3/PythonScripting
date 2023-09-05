import datetime


print(datetime.date.today())

now = datetime.datetime.today()

other = datetime.datetime(2002,9,5,21,10) # datetime(year,month,date,hours,mintues)

print(now-other)