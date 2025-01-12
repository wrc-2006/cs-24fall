'''
n=int(input())
lst=[]
for _ in range(n):
    a,b=[int(x) for x in input().split()]
    lst.append([a,b])
for i in range(n):
    for j in range(i+1,n):
        if (lst[i][0]-lst[j][0])*(lst[i][1]-lst[j][1])<0:
            print('Happy Alex')
            break
    else:
        continue    
    break           
else:
    print('Poor Alex')
'''
###忘了还有个continue，天知道为了这几个break我花了多长时间
###但是还是TLE了，好好好

n=int(input())
lst=[]
for _ in range(n):
    a,b=[int(x) for x in input().split()]
    lst.append([a,b])
lst.sort(reverse=True)
for i in lst[1:]:
    if lst[0][1]<i[1]:
        print('Happy Alex')
        break
    lst[0][1]=i[1]
else:
    print('Poor Alex')