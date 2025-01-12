# pylint: skip-file
def dfs(x,y,step):
    global ans
    if step==n*m:
        ans+=1
        return
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m and lst[nx][ny]==0:
            lst[x][y]=1
            dfs(nx,ny,step+1)
            lst[x][y]=0

t=int(input())
for _ in range(t):
    n,m,x,y=[int(x) for x in input().split()]
    direction=[(-1,2),(-1,-2),(-2,1),(-2,-1),(1,2),(1,-2),(2,1),(2,-1)]
    lst=[[0]*m for _ in range(n)]
    lst[x][y]=1
    ans=0
    dfs(x,y,1)
    print(ans)
