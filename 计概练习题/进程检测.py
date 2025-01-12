k=int(input())
for _ in range(k):
    n=int(input())
    ans=1
    lst=[]
    for __ in range(n):
        s,d=[int(x) for x in input().split()]
        lst.append([s,d])
    lst.sort()
    limit_time=lst[0]
    for i in lst[1:]:
        if limit_time[0]<=i[0]<=limit_time[1]:
            limit_time=[i[0],min(limit_time[1],i[1])]
        else:
            ans+=1
            limit_time=i
    print(ans)
    