List1 = [10, 45, 34, 20, 11]
List2 = [11, 25, 45, 20]
List3 = [20, 25, 11, 14, 45, 65]
a=set(List1)
b=set(List2)
c=set(List3)
d=a.intersection(b)
e=d.intersection(c)
print(e)
