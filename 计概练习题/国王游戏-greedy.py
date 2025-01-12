n=int(input())
a,b=[int(x) for x in input().split()]
minister=[]
for i in range(n):
    minister.append([int(x) for x in input().split()])
minister.sort(key=lambda x:x[0]*x[1])
dp=[0]*n
dp[0]=a
ans=a//minister[0][1]
for i in range(1,n):
    dp[i]=dp[i-1]*minister[i-1][0]
    ans=max(ans,dp[i]//minister[i][1])
print(ans)