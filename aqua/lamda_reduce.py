from functools import reduce


def demo1():
    n = range(1, 6)
    sum = 0
    for i in n:
        sum += i
    return sum


def demo1r():
    n = range(1, 6)
    sum = reduce(lambda cv, v: cv + v, n)
    return sum


if __name__ == '__main__':
    print(demo1())
    print(demo1r())
