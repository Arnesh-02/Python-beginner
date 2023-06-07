"Find whether triangle or not"
def tri(a,b,c):
    if(a+b>c and b+c>a and c+a>b):
        return 1
    else:
        return 0

a=float(input("Enter side 1:"))
b=float(input("Enter side 2:"))
c=float(input("Enter side 3:"))
if(tri(a,b,c)==0):
    print("Triangle is possible")
else:
    print("Triangle is not posiible")
