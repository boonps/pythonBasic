# เข้าใจการทำงานของ Python interpreter ในการกำหนดค่าให้กับตัวแปร  __name__
# เทคนิคการใช้ __name__ เมื่อโปรแกรมมีการ import module อื่นเข้ามาใช้งาน

import area


def kg_pound(kg):
    return 2.204 * kg


if __name__ == '__main__':
    print(kg_pound(10))
    print(area.rectangle(4, 6))
