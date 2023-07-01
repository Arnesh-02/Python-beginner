list= []
while True:
    num = int(input("Enter a number (or 0 to stop): "))
    if num == 0:
        break
    list.append(num)

print("Entered list:",list)

# loop to traverse each element in the list
# and, remove elements
# which are EVEN (divisible by 2)
for i in list:
    if i % 2 == 0:
        list.remove(i)

# print list after removing EVEN elements
print("List after removing EVEN numbers:")
print(list)
