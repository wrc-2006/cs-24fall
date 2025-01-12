m,n,p,q=[int(x) for x in input().split()]
lst_n=[]
lst_q=[]
for _ in range(m):
    lst_n.append([int(x) for x in input().split()])
for _ in range(p):
    lst_q.append([int(x) for x in input().split()])
for i in range(m-p+1):
    ans=[]
    for j in range(n-q+1):
        element=0
        for a in range(p):
            for b in range(q):
                element+=lst_n[i+a][j+b]*lst_q[a][b]
        ans.append(element)
    print(*ans)
    
