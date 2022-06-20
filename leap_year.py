def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

def value_year():
    value = (int(input('year = ')))
    return value


print(leap_year(value_year()))