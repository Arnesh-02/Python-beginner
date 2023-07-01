str1=input("Enter word:")
b=str1.split( )
print(b)
max_len=0
for i in b:
    c=len(i)
    if c>max_len:
        max_len=c
print("Maximum length of word:",max_len)
for i in b:
    if len(i)==max_len:
        print(i)
