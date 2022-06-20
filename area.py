def rectangle(w, h):
    # code block
    # ทำงานแบบเยื้อง indent
    area = w*h
    return area

def triangle (w,h):
    # area = .5 * w * h
    return .5 * w * h


# main entry point เริ่ม run บรรทัดนี้ เพราะ ถ้ายังไม่ประกาศเรียก def มาใช้ก็ยังไม่รัน
print("1. rectangle area")
print("2. triangle area")
n = input("please select = ")
w = int(input('width = '))
h = int(input('height = '))
if n == "1":
    print(rectangle(w, h))
else:
    print(triangle(w, h))
