even_count = 0
odd_count = 0
mylist = []
while True:
    num = int(input("Enter a number (-1 to stop): "))
    mylist.append(num)
    if num == -1:
        break
for i in mylist:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("No of odd numbers:", odd_count)
print("No of even numbers:", even_count)
