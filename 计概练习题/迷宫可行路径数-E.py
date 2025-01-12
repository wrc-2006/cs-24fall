def dfs(x,y):
    global ans
    for a,b in direction:
        nx,ny=x+a,y+b
        if nx==n-1 and ny==m-1:
            ans+=1
            continue
        if 0<=nx<n and 0<=ny<m and lst[nx][ny]==0:
            lst[x][y]=1
            dfs(nx,ny)
            lst[x][y]=0
    return

n,m=[int(x) for x in input().split()]
lst=[]
for _ in range(n):
    lst.append([int(x) for x in input().split()])
direction=[(1,0),(0,1),(-1,0),(0,-1)]
ans=0
dfs(0,0)
print(ans)