from collections import deque
def bfs(x1,y1,x2,y2):
    inq=set()
    inq.add((x1,y1,0))
    q=deque([(x1,y1,0)])
    d=[(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        x,y,time=q.popleft()
        for a,b in d:
            nx,ny=x+a,y+b
            if nx==x2 and ny==y2:
                return time+1
            if 0<=nx<r and 0<=ny<c:
                if (time+1)%k!=0:
                    if (nx,ny,(time+1)%k) not in inq and lst[nx][ny]!='#':
                        inq.add((nx,ny,(time+1)%k))
                        q.append((nx,ny,time+1))
                else:
                    if (nx,ny,time%k) not in inq:
                        q.append((nx,ny,time+1))
                        inq.add((nx,ny,(time+1)%k))
                        

for _ in range(int(input())):
    r,c,k=[int(x) for x in input().split()]
    lst=[]
    for __ in range(r):
        lst.append(input())
    for i in range(r):
        if 'S' in lst[i]:
            x1,y1=i,lst[i].index('S')
        if 'E' in lst[i]:
            x2,y2=i,lst[i].index('E')
    ans=bfs(x1,y1,x2,y2)
    if ans==None:
        print('Oop!')
    else:
        print(ans)
    