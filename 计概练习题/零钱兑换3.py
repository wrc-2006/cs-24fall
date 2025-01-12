n,m=[int(x) for x in input().split()]
coin=[int(x) for x in input().split()]
dp=[0]+[float('inf')]*m
for i in range(1,m+1):
    for j in coin:
        if j<=i:
            dp[i]=min(dp[i-j]+1,dp[i])
if dp[m]==float('inf'):
    print(-1)
else:
    print(dp[m])

