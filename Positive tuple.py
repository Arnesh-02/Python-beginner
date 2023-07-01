str1 = input("Enter elements separated by comma: ")
a = tuple(str1.split(","))
print(a)

b = ()
for i in a:#In Python, when you compare strings or numbers using the greater than (>) or less than (<) operators, they are compared lexicographically. For numbers, the comparison works as expected, but for strings, it compares them based on their lexicographic order (i.e., their ASCII values).
    if i > '0':
        b += (i, )

print(b)
print(type(a))


