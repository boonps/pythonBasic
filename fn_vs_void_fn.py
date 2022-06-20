def celsius_to_fah(celsuis):
    return (celsuis * 9 / 5) + 32

# print(celsius_to_fah(100))

def temperature_table(): #void return NONE
    for c in range(0, 101, 5):
        f = celsius_to_fah(c)
        print("{}C = {}F".format(c, f))

#a = temperature_table()

def menu():
    print("1. convert Celsius to Fahrenheit")
    print("2. display temperature table")
    n = input("enter choice : ")
    if n == "1":
        celsius = float(input("enter degree in Celsius: "))
        print("{}C = {}F".format(celsius, celsius_to_fah(celsius)))
    elif n == "2":
        temperature_table()

menu()
