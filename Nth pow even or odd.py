#n'th power is even or not
def check_power():
    a = int(input("Enter a number: "))
    b = int(input("Enter the power: "))

    if (a ** b) % 2 == 0:
        print(b, "power of", a, "is even.")
    else:
        print(b, "power of", a, "is odd.")

check_power()  
