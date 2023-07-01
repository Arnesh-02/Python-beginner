n=int(input("Enter no of elements:"))
a=[]
for i in range (1,n+1):
    b=int(input ("Enter elemnet:"))
    a.append(b)
print("Entered list:\n",a)
c=[]
for i in a:
    term=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            term=0
            break
    if term==1:
            c.append(i)
if c:
    print("True,prime no present")
else:
    print("False,prime no not present")
    
