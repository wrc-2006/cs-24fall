n=int(input())
a=[int(x) for x in input().split()]
cnt=[0]*100001
for i in a:
    cnt[i]+=1
dp=[0]*100001
dp[1]=cnt[1]
for i in range(1,100001):
    dp[i]=max(dp[i-1],dp[i-2]+i*cnt[i])
print(max(dp))