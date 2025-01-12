while True:
    a,b=[int(x) for x in input().split()]
    if a==b==0:
        break
    cnt=1
    a,b=max(a,b),min(a,b)
    while a/b<2 and a!=b:
        cnt+=1
        a,b=b,a-b
    if cnt%2==0:
        print('lose')
    else:
        print('win')