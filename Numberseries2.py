n=int(input("Enter no of terms:"))
x=int(input("Enter X:"))
def term(n,x):
    sum=0
    denominator=2
    for i in range(x,n):
        term=x/denominator
        sum+=term
        denominator*=2
    print("Sum of the series x/2+.. is=",sum)
term(n,x)    
