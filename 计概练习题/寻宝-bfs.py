#pylint:skip-file

import sys
sys.setrecursionlimit(1<<30)

def dfs(x,y):
    global minstep,step
    if lst[x][y]==1:
        if minstep>step:
            minstep=step
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<m and 0<=ny<n and lst[nx][ny]!=2 and not visited[nx][ny]:
            visited[x][y]=True
            step+=1
            dfs(nx,ny)
            step-=1
            visited[x][y]=False
        
m,n=[int(x) for x in input().split()]
lst=[[int(x) for x in input().split()] for _ in range(m)]
visited=[[False]*n for i in range(m)]
direction=[(0,1),(0,-1),(1,0),(-1,0)]
minstep,step=100000,0
dfs(0,0)
print('NO' if minstep==100000 else minstep)