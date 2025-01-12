while True:
    r,n=[int(x) for x in input().split()]
    if r==-1:
        break
    x=sorted([int(x) for x in input().split()])
    ans=0
    i=0
    while i!=n:
        army=x[i]
        i+=1
        while x[i]-army<=r:
            i+=1
        army=x[i-1]
        ans+=1
        while x[i]-army<=r:
            i+=1
    print(ans)
