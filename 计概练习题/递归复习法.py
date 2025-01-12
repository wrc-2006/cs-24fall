dp=[0]*26
dp[1],dp[2]=1,2
for i in range(3,26):
    dp[i]=dp[i-1]+dp[i-2]+i
m=int(input())
for _ in range(m):
    n=int(input())
    print(dp[n])