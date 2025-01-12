m=int(input())
for _ in range(m):
    a,b,c,d=[int(x) for x in input().split()]
    flag=False
    for j in [-a,a]:
        for k in [-b,b]:
            for p in [-c,c]:
                for q in [-d,d]:
                    if j+k+p+q==24:
                        flag=True
    print('YES' if flag else'NO')
    