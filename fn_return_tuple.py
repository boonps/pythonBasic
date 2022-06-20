def price_with_vat(amount):
    vat = amount * 7 / 107
    price = amount - vat
    # t = vat, price
    # return t
    return vat, price

# print(price_with_vat(102))
#
# a = price_with_vat(342)
# print(type(a))
# print("vat = ", a[0])
# print("price = ", a[1])
#
# v, p = price_with_vat(342)
# print("v = ", v)
# print("p = ", p)

def thai_area(sqwa):
    rai = sqwa // 400 # 1 ไร่ = 400 ตารางวา
    ngan = (sqwa - (rai * 400)) // 100
    wa = sqwa % 100
    return rai, ngan, wa

a= 956
print(thai_area(a))
r, n, w = thai_area(a)
print(r, n, w, sep="-")
