from datetime import date
from dateutil.relativedelta import relativedelta


def how_old_are_you(dob):
    age = relativedelta(date.today(), dob)
    print(age)
    return age.years, age.months, age.days


print(date.today())
# print(how_old_are_you(date(1995, 11, 8)))
y, m, d = how_old_are_you(date(1995, 11, 8))
print("{}year {}month {}day".format(y, m, d))
