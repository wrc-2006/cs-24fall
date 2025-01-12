t=int(input())
for _ in range(t):
    l,n=[int(x) for x in input().split()]
    location=sorted([int(x) for x in input().split()])
    earlist=max([x for x in location if x<=l/2]+[(l-x) for x in location if x>=l/2])
    latest=max(max(location),l-min(location)) 
    print(earlist,latest)
    
###蚂蚁相遇改变方向可看作错身而过，没有区别