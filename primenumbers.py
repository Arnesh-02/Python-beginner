print("Welcome user!")
print("Enter starting and ending range")
a=int(input("Enter starting value:"))
b=int(input("Enter ending value:"))
print("Prime numbers are:")
for i in range(a,b+1):
    if all(i%j!=0 for j in range(2,int(i**0.5)+1)):
           
        print(i)
