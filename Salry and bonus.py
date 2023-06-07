print("Hello user!")
exp=int(input("Enter your years of experience:"))
sry=float(input("Enter your salary:"))
def bonus(exp,sry):
    
    if(exp>=10):
        sal=sry+sry*0.1
        return sal
    elif(exp>=6 and exp<10):
        sal=sry+sry*0.08
        return sal
      
    elif(exp<6):
        sal=sry+sry*0.05
        return sal
    else:
        return sal
print("ur salary is ",bonus(exp,sry))
        
