def dfs(x,y,nowvalue):
    global maxvalue
    if x==n-1 and y==m-1 and nowvalue>maxvalue:
        maxvalue=nowvalue
        return
    visited[x][y]=True
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            dfs(nx,ny,nowvalue+lst[nx][ny])
    visited[x][y]=False

n,m=[int(x) for x in input().split()]
lst=[]
for i in range(n):
    lst.append([int(x) for x in input().split()])
maxvalue=float('-inf')
direction=[(0,1),(0,-1),(1,0),(-1,0)]
visited=[[False]*m for i in range(n)]
dfs(0,0,lst[0][0])
print(maxvalue)