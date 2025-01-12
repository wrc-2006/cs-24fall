def dfs(p,discount,selected):
    global ans,cost
    if selected==n:
        sumcost=sum(cost)
        cnt=sumcost//300
        rcost=cost[:]
        for i in range(m):
            for shopdiscount in discount[i][::-1]:
                if rcost[i]>=shopdiscount[0]:
                    sumcost-=shopdiscount[1]
                    break
                
        ans=min(ans,int(sumcost-50*cnt))
        return
    for shop,price in p[selected]:
        cost[shop-1]+=price
        dfs(p,discount,selected+1)
        cost[shop-1]-=price
    
n,m=[int(x) for x in input().split()]
p=[[]for _ in range(n)]
discount=[[]for _ in range(m)]
for _ in range(n):
    s=[x for x in input().split()]
    p[_]=[list(map(int,x.split(':'))) for x in s]   #商店，价格
for _ in range(m):
    s=[x for x in input().split()]
    discount[_]=[list(map(int,x.split('-'))) for x in s]  #满减
    discount[_].sort(key=lambda x:x[1])
ans=float('inf')
selected=0
cost=[0 for i in range(m)]
dfs(p,discount,0)
print(ans)