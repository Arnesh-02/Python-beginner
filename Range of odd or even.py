print("Hello user!")
a = int(input("Enter starting range: "))
b = int(input("Enter ending range: "))
even_count=0
odd_count=0
for i in range(a, b + 1, 1):
    if i% 2 == 0:
        even_count+=1
    else:
        odd_count+=1
print("Odd no's count:",odd_count)
print("Even no's count:",even_count)
