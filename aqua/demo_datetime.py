from datetime import date, datetime


def demo1():
    today = date.today()
    print(today)
    dt = datetime.today()
    print(dt)


demo1()


def demo2():
    songran = date(2020, 4, 13)
    print('*' * 40)
    print(songran)


demo2()

def demo3():
    d1 = datetime.strptime("20200413", "%Y%m%d")
    print(d1)
    d2 = datetime.strptime("20200413", "%Y%m%d").date()
    print(d2)
    d3 = datetime.strptime("20200413T06:45", "%Y%m%dT%H:%M")
    print(d3)

demo3()
