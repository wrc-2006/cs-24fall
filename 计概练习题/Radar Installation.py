from math import sqrt
case=0
while True:
    n,d=[int(x) for x in input().split()]
    if n==d==0:
        break
    case+=1
    ans=1
    radar=[]
    for _ in range(n):
        x,y=[int(x) for x in input().split()]
        if y>d:
            ans=-1
        else:
            m=sqrt(d*d-y*y)
            radar.append([x-m,x+m])
    radar.sort()
    if ans==-1:
        print(f'Case {case}: {ans}')
    else:
        rst,red=radar[0][0],radar[0][1]
        for st,ed in radar[1:]:
            if st>red:
                ans+=1
                rst,red=st,ed
            else:
                rst,red=st,min(ed,red)
        print(f'Case {case}: {ans}')
    input()
             
        