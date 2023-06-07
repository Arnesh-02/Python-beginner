a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = int(input("Enter no 3: "))

if a < b and b < c:
    num = (a * a) + (b * b)
    if num == (c * c):
        print(1)
    else:
        print(0)
else:
    print("Invalid input")
