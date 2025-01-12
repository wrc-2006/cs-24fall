def f(lst,m,p,kids):
    original_m=m
    while len(lst)>1:
        if m>1:
            lst.append(lst.pop(0))
            m-=1
        elif m==1:
            kids.append(str(lst.pop(0)))
            m=original_m
    if len(lst)==1:
        kids.append(str(lst[0]))
    return kids
while True:
    n,p,m=[int(x) for x in input().split()]
    if n+m+p==0:
        break
    kids=[]
    lst=[int(i) for i in range(p,n+1)]+[int(i) for i in range(1,p)]
    print(','.join(f(lst,m,p,kids)))