n,m=[int(x) for x in input().split()]
lst=[[0]*(m+2)]
for _ in range(n):
    s=[int(x) for x in input().split()]
    lst.append([0]+s+[0])
lst.append([0]*(m+2))
ans=0
for i in range(n+2):
    for j in range(m+2):
        if lst[i][j]==1:
            ans+=4-lst[i-1][j]-lst[i+1][j]-lst[i][j+1]-lst[i][j-1]
print(ans)        
