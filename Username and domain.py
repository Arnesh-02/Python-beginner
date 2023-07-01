str=input("Enter email address:")
b=str.split("@")[0]
c=tuple(b)
print("Username:",c)
d=str.split("@")[1]
print("Domain:",tuple(d))
