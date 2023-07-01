a = list(map(int, input("Enter list of elements: ").split( )))
print(a)
b=[]
import math
for i in a:
    c=math.factorial(i)
    b.append(c)
print(b)
