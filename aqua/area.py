# เข้าใจการทำงานของ Python interpreter ในการกำหนดค่าให้กับตัวแปร  __name__
# เทคนิคการใช้ __name__ เมื่อโปรแกรมมีการ import module อื่นเข้ามาใช้งาน

def rectangle(w, h):
    # code block
    # ทำงานแบบเยื้อง indent
    # area = w*h
    return w * h


def square(s):
    return s * s


if __name__ == '__main__':
    print(__name__)
    # print(rectangle(3, 4))
    w = int(input("width = "))
    h = int(input("height = "))
    print(rectangle(w, h))
