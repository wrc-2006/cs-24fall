q=int(input())
for _ in range(q):
    n=int(input())
    s=sorted([int(x) for x in input().split() if int(x)<=2048],reverse=True)
    while True:
        if len(s)<=1 and 2048 not in s:
            print('NO')
            break
        if 2048 in s:
            print('YES')
            break
        else:
            s.insert(0,s.pop(0)+s.pop(0))
