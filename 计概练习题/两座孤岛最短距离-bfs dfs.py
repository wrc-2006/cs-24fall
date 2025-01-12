from collections import deque
def dfs(x,y,island):
    lst[x][y]=2
    for a,b in d:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m:
            if lst[nx][ny]==1:
                dfs(nx,ny,island)
            if lst[nx][ny]==0:
                island.append((x,y,0))
            
def bfs(q):
    while q:
        for _ in range(len(q)):   #多源bfs
            x,y,step=q.popleft()
            for a,b in d:
                nx,ny=x+a,y+b
                if 0<=nx<n and 0<=ny<m:
                    if lst[nx][ny]==1:
                        return step
                    if lst[nx][ny]==0:
                        lst[nx][ny]=2     ##标记已访问节点！！！标记后即使不用多源bfs也可以
                        q.append((nx,ny,step+1))
                 
lst=[]
n=int(input())
for _ in range(n):
    lst.append([int(x) for x in input()])
m=len(lst[0])
d=[(0,1),(1,0),(-1,0),(0,-1)]
q=deque()
for i in range(n):
    for j in range(m):
        if lst[i][j]==1:
            dfs(i,j,q)
            newans=bfs(q)
            break
    else:
        continue
    break       
print(newans)