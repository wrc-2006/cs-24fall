while True:
    n=2
    s=1/2
    c=float(input())
    if c==0.00:
        break
    while s<c:
        n+=1
        s+=1/n
    else:
        print(n-1,'card(s)')
        