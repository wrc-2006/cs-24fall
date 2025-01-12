'''
p=[int(x) for x in input().split(',')]
ans=max(p)
dp=[0]*(len(p)+1)
dp[0]=p[0]
for i in range(1,len(p)):
    dp[i]=dp[i-1]+p[i]
for i in range(len(p)-1):
    for j in range(i+1,len(p)):
        ans=max(ans,dp[j]-dp[i-1]-min(0,min(p[i:j+1])))
print(ans)
暴力解题TLE了
'''

p=[int(x) for x in input().split(',')]
dp1,dp2=[0]*len(p),[0]*len(p)
dp1[0]=dp2[0]=p[0]
for i in range(1,len(p)):
    dp1[i]=max(p[i],dp1[i-1]+p[i])
    dp2[i]=max(p[i],dp1[i-1],dp2[i-1]+p[i])
print(max(dp2))

