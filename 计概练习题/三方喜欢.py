n,q=[int(x) for x in input().split()]
lst=[]
for _ in range(q):
    x,y=[int(x) for x in input().split()]
    lst.append([x,y])
for i in lst:
    for j in lst:
        if i[1]==j[0]:
            if [j[1],i[0]] in lst:
                print('Yes')
                break
    else:
        continue
    break
else:
    print('No')
