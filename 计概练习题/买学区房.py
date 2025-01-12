n=int(input())
d=[eval(x) for x in input().split()]
rd=[x[0]+x[1] for x in d]
p=[int(x) for x in input().split()]
distance=[]
for i in range(n):
    distance.append((rd[i]+rd[i])/p[i])
rp=sorted(p)
rdistance=sorted(distance)
if n%2!=0:
    midp=rp[n//2]
    midd=rdistance[n//2]
else:
    midp=(rp[n//2]+rp[n//2-1])/2
    midd=(rdistance[n//2]+rdistance[n//2-1])/2
ans=0
for i in range(n):
    if distance[i]>midd and p[i]<midp:
        ans+=1
print(ans)