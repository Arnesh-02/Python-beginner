a = list(map(int, input("Enter list of elements: ").split( )))
b = []
c = []

for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)

print("Even list =", b)
print("Odd list =", c)
