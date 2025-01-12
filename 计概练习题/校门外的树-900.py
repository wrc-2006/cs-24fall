l,m=map(int,input().split())
lst=[1]*(l+1)
for _ in range(m):
    p,q=[int(x) for x in input().split()]
    for i in range(p,q+1):
        lst[i]=0
print(lst.count(1))
    
