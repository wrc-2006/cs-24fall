p=int(input())
cost=sorted([int(x) for x in input().split()])
lst=[True]*(len(cost))
mine=0
enermy=0
ans=[]
i=0
j=-1
while lst!=[False]*(len(cost)):
    if lst[i]:
        if p>=cost[i]:
            p-=cost[i]
            mine+=1
            lst[i]=False
            i+=1
        else:
            if mine==enermy:
                ans.append(mine-enermy)
                break
            ans.append(mine-enermy)
            p+=cost[j]
            enermy+=1
            lst[j]=False
            j-=1
        ans.append(mine-enermy)
print(max(ans))