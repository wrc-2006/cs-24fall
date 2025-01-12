n,q=[int(x) for x in input().split()]
lst=[]
for _ in range(q):
    x,y=[int(x) for x in input().split()]
    lst.append([x,y])
for i in lst:
    if [i[1],i[0]] in lst:
        print('Yes')
        break
else:
    print('No')