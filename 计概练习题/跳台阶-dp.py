n=int(input())
dp=[0]*26
dp[1]=1
for i in range(2,26):
    dp[i]=sum(dp[:i])+1
print(dp[n])