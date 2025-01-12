t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    mina=min(a)
    minb=min(b)
    min1=sum([mina+m for m in b])
    min2=sum([minb+n for n in a])
    print(min(min1,min2))