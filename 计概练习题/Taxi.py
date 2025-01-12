import math
n=int(input())
kids=[int(x) for x in input().split()]
a,b,c,d=map(kids.count,(1,2,3,4))
ans=d+c
a=max(0,a-c)
ans+=math.ceil((b*2+a)/4)
print(ans)

