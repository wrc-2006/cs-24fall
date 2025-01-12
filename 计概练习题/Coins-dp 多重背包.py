while True:
    n,m=[int(x) for x in input().split()]
    if n==0:
        break
    lst=[int(x) for x in input().split()]
    coin=lst[:n]
    num=lst[n:]
    newlst=[]
    for i in range(n):
        newlst+=[coin[i]]*num[i]
    newlst.sort()
    dp=[0]+[-float('inf')]*m
    for i in range(n):
        for j in range(m,newlst[i]-1,-1):
            dp[j]=max(dp[j],dp[j-newlst[i]]+1)
    cnt=0
    for i in dp:
        if i!=0:
            cnt+=1
    print(cnt)
     