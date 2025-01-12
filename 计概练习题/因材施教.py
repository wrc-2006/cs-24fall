'''
n,m=[int(x) for x in input().split()]
r=sorted([int(x) for x in input().split()])
difference=sorted([r[i+1]-r[i] for i in range(n-1)])
cnt,i=m-1,-1
ans=sum(difference)
while cnt!=0:
    ans-=difference[i]
    i-=1
    cnt-=1
print(ans)
'''
n,m=[int(x) for x in input().split()]
rank=sorted([int(x) for x in input().split()])
lst=[rank[i]-rank[i-1] for i in range(1,n)]
lst.sort()
print(sum(lst[:len(lst)-m+1]))
