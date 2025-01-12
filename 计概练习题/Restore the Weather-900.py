'''
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    lst=[]
    for ai in a:
        for bi in b:
            if abs(bi-ai)<=k:
                lst.append(bi)
                b.remove(bi)
                break
    print(*lst)
'''
t=int(input())
for _ in range(t):
    n,k=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    v=[(a[i],i) for i in range(n)]
    v.sort()
    b.sort()
    lst=[0]*n
    for i in range(n):
        lst[v[i][1]]=b[i]
    print(*lst)