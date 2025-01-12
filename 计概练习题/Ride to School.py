import math
while True:
    n=int(input())
    if n==0:
        break
    lst=[]
    for _ in range(n):
        v,t=[int(x) for x in input().split()]
        if t<0:
            continue
        time=math.ceil((4.5/v)*3600)+t
        lst.append(time)
    print(min(lst))