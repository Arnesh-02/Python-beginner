a=set()
for i in range(1,31):
        c=i**2
        a.add(c)
print("Squares of number:")
print(a)
b=set()
for i in range(1,31):
    if i%3==0:
          b.add(i)
print("Numbers divisible by 3:")
print(b)
print("Elements in square set removing numbers divisible by 3:")
print(a-b)
