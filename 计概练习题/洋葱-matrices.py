from math import ceil
n=int(input())
lst=[]
for _ in range(n):
    lst.append([int(x) for x in input().split()])
d=[(0,1),(1,0),(0,-1),(-1,0)]
ans=0
for i in range(ceil(n/2)):
    cnt=0
    newans=lst[i][i]
    lst[i][i]=0
    x,y=i,i
    while cnt!=4:
        num=1
        a,b=d[cnt]
        while num<n-i*2:
            x+=a
            y+=b
            newans+=lst[x][y]
            num+=1
        cnt+=1
    ans=max(ans,newans)
print(ans)
    

