n,a,b,c=[int(x) for x in input().split()]
s=[a,b,c]
dp=[0]+[-100000]*n  #直接全设为0最后结果可能n并没有完全划分
for i in range(1,n+1):
    for j in s:
        if i>=j:
            dp[i]=max(dp[i],dp[i-j]+1)
print(dp[n])

'''
需要刚好装满的背包问题，a，b，c的价值为1，求最大价值
'''