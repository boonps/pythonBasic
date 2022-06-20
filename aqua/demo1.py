#การเรียกใช้โค้ด python จากที่อื่นๆ
import sys

# import area

# print(sys.path)
# print(area)
from body_mass_index import Bmi

peter = Bmi(70, 180)
print(peter.bmi, peter.category())
