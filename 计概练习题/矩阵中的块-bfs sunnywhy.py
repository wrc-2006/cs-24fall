'''
dfs又超时又爆栈 还是得用bfs

import sys
sys.setrecursionlimit(1<<30)

def dfs(x,y):
    lst[x][y]=0
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m and lst[nx][ny]==0:
            dfs(nx,ny)

n,m=[int(x) for x in input().split()]
lst=[]
for _ in range(n):
    lst.append([int(x) for x in input().split()])
direction=[(1,0),(0,1),(-1,0),(0,-1)]
cnt=0
for i in range(n):
    for j in range(m):
        if lst[i][j]==1:
            cnt+=1
            dfs(i,j)
print(cnt)
'''
    
from collections import deque
def bfs(x,y):
    inq.add((x,y))
    q=deque([(x,y)])
    while q:
        front=q.popleft()
        for a,b in direction:
            nx,ny=front[0]+a,front[1]+b
            if 0<=nx<n and 0<=ny<m:
                if lst[nx][ny]==1 and (nx,ny) not in inq:
                    q.append((nx,ny))
                    inq.add((nx,ny))
            
n,m=[int(x) for x in input().split()]
lst=[]
for _ in range(n):
    lst.append([int(x) for x in input().split()])
direction=[(0,1),(0,-1),(1,0),(-1,0)]
cnt=0
inq=set()
for i in range(n):
    for j in range(m):
        if lst[i][j]==1 and (i,j) not in inq:
            bfs(i,j)
            cnt+=1
print(cnt)


