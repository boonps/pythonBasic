# การบวก ลบ เวลาที่มีหน่วยเป็นวัน เดือน ปี สัปดาห์ ชั่วโมง นาที เช่น
# อีก 90 วันจากวันนี้จะเป็นวันที่เท่าไร
# อีก 1 ปี 3 เดือน 7 วัน จากวันนี้จะเป็นวันอะไร
# หาว่าวันเสาร์ที่สองของเดือนมกราคมตรงกับวันที่เท่าไร
# จากเวลานี้ไปอีก 3 ชั่วโมงเป็นเวลาเท่าไร

# pip install python-dateutil
from datetime import datetime, date

from dateutil.relativedelta import relativedelta, SA, TH


def demo1():
    today = date.today()
    next_3_m = today + relativedelta(months=3)
    print(today)
    print(next_3_m)

    d1 = today + relativedelta(weeks=40)
    print(d1)

    d2 = today + relativedelta(years=1, months=6)
    print(d2)

    d3 = today + relativedelta(days=-1)
    print(d3)


def demo2():
    now = datetime.today()
    print(now)
    t1 = now + relativedelta(hours=3, minutes=30)
    print(t1)


def demo_weekday():
    childrenday = date(2016, 1, 1) + relativedelta(weekday=SA(+2))
    print(childrenday)
    print(datetime.strftime(childrenday, "%a %b %d %m %y"))
    thanksgiving = date(2016, 11, 1) + relativedelta(weekday=TH(4))
    print(datetime.strftime(thanksgiving, "%a %b %d-%m-%Y"))


def demo3():
    d1 = date(2016, 3, 31)
    d2 = d1 + relativedelta(months=1)
    d3 = d2 + relativedelta(months=-2)
    print(d2)
    print(d3)


# demo1()
# demo2()
# demo_weekday()
demo3()
