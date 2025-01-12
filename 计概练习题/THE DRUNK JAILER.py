t=int(input())
for _ in range(t):
    n=int(input())
    s=[True]*n #True对应lock False对应unlock
    for i in range(1,n+1):
        for a in range(1,n+1):
            if a%i==0:
                s[a-1]=not s[a-1]
    print(s.count(False))