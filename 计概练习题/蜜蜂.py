def bee(d,dp):
    if dp[d]!=0:
        return dp[d]
    else:
        dp[d]=bee(d-1,dp)+bee(d-2,dp)
        return dp[d]
n=int(input())
dp=[0]*22
dp[2],dp[3]=1,2
for _ in range(n):
    a,b=[int(x) for x in input().split()]
    print(bee(b-a+1,dp))
    