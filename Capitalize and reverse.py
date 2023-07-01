str1=input("Enter a string:")
b=len(str1)
if b%5==0:
    print("Reversed string:\n")
    print(str1[::-1])
    print("Captitalized string:\n")
    print(str1.upper())
else:
    print("Length of string not a factorial of 5")
