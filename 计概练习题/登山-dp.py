n=int(input())
h=[0]+[int(x) for x in input().split()]
dp1=[0]*(n+1)   #dp1[i]:i前（不包括i）最大上升
dp2=[1]*(n+1)   #dp2[i]:i后（包括i）最大下降
for i in range(2,n+1):
    for j in range(1,i):
        if h[j]<h[i]:
            dp1[i]=max(dp1[i],dp1[j]+1)
for i in range(n,1,-1):
    for j in range(i+1,n+1):    ##或range(n,i,-1)也行
        if h[j]<h[i]:
            dp2[i]=max(dp2[i],dp2[j]+1)
ans=[0]*(n+1)
for i in range(n+1):
    ans[i]=dp1[i]+dp2[i]
print(max(ans))
