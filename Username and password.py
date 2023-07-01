str1=input("Enter your mail id:")
a=str1.split("@")[0]
print("Username:",a)
b=a+a[::-1]
print("Password:",b)
