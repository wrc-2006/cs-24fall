import sys
sys.setrecursionlimit(1<<20)
##防止递归深度过大导致RE

def dfs(x,y):
    direction=[(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]
    field[x][y]='.'
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m and field[nx][ny]=='W':
            dfs(nx,ny)
        

n,m=map(int,input().split())
field=[list(input()) for _ in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if field[i][j]=='W':
            ans+=1
            dfs(i,j)
print(ans)