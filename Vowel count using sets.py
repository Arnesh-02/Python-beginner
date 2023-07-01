VOWELS = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}
str1=input("Enter a string:")
count=0
for i in str1:
    if i in VOWELS:
        count+=1
print(count)
    
