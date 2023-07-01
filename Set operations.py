a=set()
for i in range(1,51):
    if i%5==0:
        a.add(i)
print("Numbers divisible by 5:")
print(a)
b=set()
for i in range(2,51):#The reason we typically start the range from 2 instead of 0 or 1 when checking for prime numbers is that 0 and 1 are not considered prime numbers. By convention, prime numbers are defined as numbers greater than 1 that have no divisors other than 1 and themselves.
    for j in range(2,int(i**0.5)+1):
        result=1
        if i%j==0:
            result=0
            break
        if result:
          b.add(i)
print("Prime numbers:")
print(b)
print("Union:\n",a.union(b))
print("Intersection:\n",a.intersection(b))
print("Set difference:\n",a.difference(b))
print("Symmetric difference:\n",a.symmetric_difference(b))
