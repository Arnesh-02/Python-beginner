n=int(input("Enter no of terms:"))
def fibo(n):
    a={0:0,1:1}
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
    return a[n]
b=fibo(n)
print('Fibonacci series value',b)

     
