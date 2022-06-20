import datetime


def dat_format_demo():
    d = datetime.date(2020, 4, 12)
    print(d.strftime("%d-%m-%y"))
    fmt = [
        "%d/%m/%y",
        "%a %d %b %Y",
        "%A %D %B %Y",
        "%d %b %y"
    ]
    for f in fmt:
        print("{:20} ---> {}".format(f, d.strftime(f)))


def time_format_demo():
    d = datetime.datetime(2020, 4, 12, 16, 28, 45)
    print(d)
    print(d.strftime("%d-%m-%y %H:%M:%S"))
    fmt = [
        "%d/%m/%y",
        "%a %d %b %Y %I:%m%p",
        "%A %D %B %Y",
        "%d %b %y"
    ]
    for f in fmt:
        print("{:20} ---> {}".format(f, d.strftime(f)))


# dat_format_demo()
time_format_demo()
