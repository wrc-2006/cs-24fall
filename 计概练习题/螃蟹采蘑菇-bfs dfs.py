'''
def dfs(x1,y1,x2,y2,tx,ty):
    if (x1==tx and y1==ty) or (x2==tx and y2==ty):
        return 'yes'
    ans='no'
    visited[x1][y1]=True
    visited[x2][y2]=True
    for a,b in d:
        nx1,ny1,nx2,ny2=x1+a,y1+b,x2+a,y2+b
        if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0<=ny2<n:
            if lst[nx1][ny1]!=1 and lst[nx2][ny2]!=1:
                if (not visited[nx1][ny1]) or (not visited[nx2][ny2]):
                    ans=dfs(nx1,ny1,nx2,ny2,tx,ty)
                    if ans=='yes':
                        return ans     
    return 'no'
n=int(input())
lst=[]
position=[]
for _ in range(n):
    s=[int(x) for x in input().split()]
    lst.append(s)
    if 5 in s:
        position.append((_,s.index(5)))
        lst[_][s.index(5)]=0
    if 5 in s:
        position.append((_,s.index(5)))
        lst[_][s.index(5)]=0
    if 9 in s:
        tx,ty=_,s.index(9)
d=[(0,1),(1,0),(-1,0),(0,-1)]
x1,y1=position[0]
x2,y2=position[1]
visited=[[False]*n for i in range(n)]
print(dfs(x1,y1,x2,y2,tx,ty))
'''
from collections import deque
def bfs(x1,y1,x2,y2):
    inq=set((x1,y1))
    inq.add((x2,y2))
    q=deque([(x1,y1,x2,y2)])
    while q:
        x1,y1,x2,y2=q.popleft()
        if lst[x1][y1]==9 or lst[x2][y2]==9:
            return 'yes'
        for a,b in d:
            nx1,ny1,nx2,ny2=x1+a,y1+b,x2+a,y2+b
            if 0<=nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n:
                if (nx1,ny1) not in inq or (nx2,ny2) not in inq:
                    if lst[nx1][ny1]!=1 and lst[nx2][ny2]!=1:
                        inq.add((nx1,ny1))
                        inq.add((nx2,ny2))
                        q.append((nx1,ny1,nx2,ny2))
    return 'no'
    
n=int(input())
lst=[]
position=[]
for _ in range(n):
    s=[int(x) for x in input().split()]
    lst.append(s)
    if 5 in s:
        position.append((_,s.index(5)))
        lst[_][s.index(5)]=0
    if 5 in s:
        position.append((_,s.index(5)))
        lst[_][s.index(5)]=0
    if 9 in s:
        tx,ty=_,s.index(9)
d=[(0,1),(1,0),(-1,0),(0,-1)]
x1,y1=position[0]
x2,y2=position[1]
visited=[[False]*n for i in range(n)]
print(bfs(x1,y1,x2,y2))