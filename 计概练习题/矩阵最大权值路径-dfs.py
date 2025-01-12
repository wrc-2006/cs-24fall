def dfs(x,y,nowvalue):
    global maxvalue,maxpath
    if x==n-1 and y==m-1:
        if nowvalue>maxvalue:
            maxvalue=nowvalue
            maxpath=path[:]
            return 
    visited[x][y]=True
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            path.append((nx+1,ny+1))
            dfs(nx,ny,nowvalue+lst[nx][ny])
            path.pop()
    visited[x][y]=False

n,m=[int(x) for x in input().split()]
lst=[]
for i in range(n):
    lst.append([int(x) for x in input().split()])
maxvalue=float('-inf')
direction=[(0,1),(0,-1),(1,0),(-1,0)]
visited=[[False]*m for i in range(n)]
path=[(1,1)]
dfs(0,0,lst[0][0])
for i in maxpath:
    print(*i)
