'''
n,b=[int(x) for x in input().split()]
price=[int(x) for x in input().split()]
weight=[int(x) for x in input().split()]
dp=[0]*(b+1)   #用于存储不同重量下的最大价值
for i in range(n):
    for j in range(b,weight[i]-1,-1):
        dp[j]=max(dp[j],dp[j-weight[i]]+price[i])
print(dp[-1])
'''
#或使用二维数组

n,b=[int(x) for x in input().split()]
price=[int(x) for x in input().split()]
weight=[int(x) for x in input().split()]
cell=[[0 for i in range(b+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,b+1):
        if j>=weight[i-1]:
            cell[i][j]=max(cell[i-1][j],cell[i-1][j-weight[i-1]]+price[i-1])
        else:
            cell[i][j]=cell[i-1][j]
print(cell[n][b])


'''
cell=[[0]*(b+1)]*(n+1)浅拷贝问题，不能这样写
'''