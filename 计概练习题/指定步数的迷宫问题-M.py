'''
辅助visited空间
'''

def dfs(x,y,visited):
    global ans,k
    if x==n-1 and y==m-1 and k==0:
        ans='Yes'
    visited[x][y]=True
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False and lst[nx][ny]==0:
            k-=1
            dfs(nx,ny,visited)
            k+=1
    visited[x][y]=False
    
    
n,m,k=[int(x) for x in input().split()]
lst=[]
direction=[(1,0),(0,1),(-1,0),(0,-1)]
for _ in range(n):
    lst.append([int(x) for x in input().split()])
visited=[[False]*m for i in range(n)]
ans='No'
dfs(0,0,visited)
print(ans)