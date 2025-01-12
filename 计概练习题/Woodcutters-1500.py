n=int(input())
lst=[]
for _ in range(n):
    x,h=map(int,input().split())
    lst.append([x,h])
ans=min(n,2)
for i in range(1,n-1):
    if lst[i][1]<lst[i][0]-lst[i-1][0]:
        ans+=1
        continue
    elif lst[i][1]<lst[i+1][0]-lst[i][0]:
        ans+=1
        lst[i][0]+=lst[i][1]
print(ans)