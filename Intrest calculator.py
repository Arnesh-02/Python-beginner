Name=input("Enter name:")
age=int(input("Enter age:"))
gender=input("Enter gender:")
def intrest_calculation(Name,age,gender):
 print("Hello!",Name)
 p=float(input("Enter principal amount:"))
 n=int(input("Enter no of years:"))
 if(age>60):
     r=0.12
     return p*n*r
 elif(gender=="F" or gender=="f"):
     r=0.1
     return p*n*r
 else:
     r=0.9
     return p*n*r
print("Your intrest rate=",intrest_calculation(Name,age,gender))
