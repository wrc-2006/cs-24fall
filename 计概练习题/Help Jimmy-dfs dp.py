def jimmy(x,y,platform,maxh):
    lst=sorted([x for x in platform if x[2]<=y],key=lambda x:x[2],reverse=True)
    ans=y-lst[0][2]
    if len(lst)==1:
        if lst[0][0]<=x<=lst[0][1]:
            return y+min(x-lst[0][0],lst[0][1]-x)
        else:
            return y
    
         
        

t=int(input())
for _ in range(t):
    n,x,y,maxh=[int(x) for x in input().split()]
    platform=[]
    for __ in range(n):
        x1,x2,h=[int(x) for x in input().split()]
        platform.append([x1,x2,h])
    