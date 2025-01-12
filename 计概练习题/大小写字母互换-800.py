s=input()
m=''
for i in s:
    if i.isupper():
        m+=i.lower()
    else:
        m+=i.upper()
print(m)