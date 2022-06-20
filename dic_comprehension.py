#  /- สร้าง dictionary จาก tuple ที่เก็บอยู่ใน list ด้วย dict comprehensions
# -สร้าง dictionary โดย zip() ข้อมูลที่อยู่ใน list 2 ตัวเข้าด้วยกัน โดย list ตัวแรกทำหน้าที่เป็น key ส่วน list
#  ตัวที่สองทำหน้าที่เป็น value

import datetime


def demo1():
    t = [("sun", "red"), ("mon", "yellow"), ("tue", "pink"), ("wed", "green"),
         ("thu", "orange"), ("fri", "blue"), ("sat", "purple")]
    d = {}
    for k, v in t:
        d[k] = v
    print(d)

    d1 = {k.capitalize(): v for k, v in t}  # dict comprehensions
    print(d1)

    today = datetime.datetime.now()
    print(today.strftime("%a"))
    weekday = today.strftime("%a")
    weekcolor = d1[weekday]
    print(weekday, weekcolor)


def demo2():
    weekdays = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
    weekcolors = ["red", "yellow", "pink", "green", "orange", "blue", "purple"]
    t = zip(weekdays, weekcolors)  # generators
    d1 = {k.capitalize(): v for k, v in t}  # dict comprehensions
    print(d1)


# demo1()
demo2()