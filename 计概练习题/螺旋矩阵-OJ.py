k=int(input())
arr=[[0]*k for i in range(k)]
lst=[[1000]*(k+2)]+[[1000]+i+[1000] for i in arr]+[[1000]*(k+2)]
i,j=1,1
direction=[[0,1],[1,0],[0,-1],[-1,0]]
index=0
dire=direction[0]
m,n=dire
num=1
while num<=k**2:
    if lst[i][j]<1000:
        arr[i-1][j-1]=num
        num+=1
        lst[i][j]=1000
        i+=m
        j+=n
    else:
        index=(index+1)%4
        dire=direction[index]
        i-=m
        j-=n
        m,n=dire
        i+=m
        j+=n
for i in arr:
    print(*i)