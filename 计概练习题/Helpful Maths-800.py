s=input()
lst=[]
for i in s:
    if i !='+':
        lst.append(i)
lst.sort()
print('+'.join(lst))
    
