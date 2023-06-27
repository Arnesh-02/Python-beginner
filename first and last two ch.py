str_1 = input("Enter a string: ")
str_2 = ""
term = 0

for i in str_1:
    term += 1
    if term <=2:
        str_2 += i
    if term==len(str_1)-1 or term==len(str_1):
        str_2+=i

print(str_2)
