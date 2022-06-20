# การเรียงลำดับข้อมูลภาษาไทย (sort Thai character)

import pyuca

province = ["พิษณุโลก", "ชัยนาท", "เลย", "เพชรบุรี", "ลำปาง", "ขอนแก่น", "กรุงเทพ", "เชียงใหม่", "ตาก", "แพร่"]
s = sorted(province)
print(s)

s_correct = sorted(province, key=pyuca.Collator().sort_key)
print(s_correct)
print(province)
province.sort(key=pyuca.Collator().sort_key)
print(province)