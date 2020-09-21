import p15
import math
import os
import calendar
from datetime import date
from datetime import  datetime

today=date.today()
now=datetime.now()

d1=today.strftime("%d%m%y")

print("todays date",today)
print("d1=",d1)

from p15 import add,subtract
print  (p15.add(10, 2))

year=2020
mm=9

print (calendar.month(year,mm))

print(calendar.calendar(2020,2,1,6))

print(math.sqrt(25))

print(p15.subtract(15,2))

print (subtract(10,5))


print(os.getcwd())