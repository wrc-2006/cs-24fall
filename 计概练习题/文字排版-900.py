n=int(input())
article=input().split()
lst1=[]
lst2=article[0]+' '
for i in article[1:]:
    if len(lst2+i)<=80:
        lst2+=i+' '
    else:
        lst1.append(lst2.rstrip())
        lst2=i+' '
lst1.append(lst2.rstrip())
print('\n'.join(lst1))