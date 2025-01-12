'''
bfs tle失败
from collections import deque
def bfs(x,y):
    q=deque([(x,y,1)])
    visited[x][y]=True
    while q:
        x,y,step=q.popleft()
        for a,b in d:
            nx,ny=x+a,y+b
            if 0<=nx<r and 0<=ny<c:
                if h[nx][ny]<h[x][y]:    
                    q.append((nx,ny,step+1))
    return step
    
r,c=[int(x) for x in input().split()]
h=[]
for _ in range(r):
    h.append([int(x) for x in input().split()])
d=[(0,1),(1,0),(-1,0),(0,-1)]
out=0
visited=[[False]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            out=max(out,bfs(i,j))
print(out)
'''
import sys
from functools import lru_cache
sys.setrecursionlimit(1<<30)
@lru_cache(maxsize=None)
def dfs(x,y):
    step=1
    for a,b in d:
        nx,ny=x+a,y+b
        if 0<=nx<r and 0<=ny<c and h[nx][ny]<h[x][y]:
            step=max(step,1+dfs(nx,ny))
    return step

r,c=[int(x) for x in input().split()]
h=[]
for _ in range(r):
    h.append([int(x) for x in input().split()])
d=[(0,1),(1,0),(-1,0),(0,-1)]
out=0
for i in range(r):
    for j in range(c):
        out=max(out,dfs(i,j))
print(out)


