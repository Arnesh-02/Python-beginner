a=list(map(int,input("Enter elements:").split( )))
print("Entered list:",a)
b=[]
for i in a:
    if i not in b:
        b.append(i)
print("list without duplicates:",b)
    
