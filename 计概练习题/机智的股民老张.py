'''
a=[int(x) for x in input().split()]
dp=[0]*(len(a))
dp[-1]=a[-1]
for i in range(len(a)-2,-1,-1):
    dp[i]=max(dp[i+1],a[i])
ans=0
for i in range(len(a)-1):
    ans=max(ans,dp[i]-a[i])
print(ans)

dp[i]表示a中i之后（包含i）的最大值
'''

a=[int(x) for x in input().split()]
dp=[0]*(len(a))
dp[0]=a[0]
for i in range(1,len(a)):
    dp[i]=min(dp[i-1],a[i])
ans=0
for i in range(1,len(a)-1):
    ans=max(ans,a[i]-dp[i-1])
print(ans)

#dp[i]表示a中i之前（包含i）的最小值