t,k=[int(x) for x in input().split()]
dp=[1]*100001
s=[1]*100001
for i in range(1,100001):   
    if i>=k:
        dp[i]=(dp[i-1]+dp[i-k])%1000000007
    s[i]=(s[i-1]+dp[i])%1000000007
for _ in range(t):
    a,b=[int(x) for x in input().split()]
    print((s[b]-s[a-1])%1000000007)


