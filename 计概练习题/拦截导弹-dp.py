k=int(input())
height=[int(x) for x in input().split()]
dp=[1]*k
for i in range(1,k):
    for j in range(i):
        if height[j]>=height[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
