from collections import deque
def bfs(x,y):
    inq=set()
    inq.add((x,y))
    q=deque([(x,y,0)])
    while q:
        first,second,step=q.popleft()
        if first==n-1 and second==m-1:
            return step
        for a,b in direction:
            nx,ny=first+a,second+b
            if 0<=nx<n and 0<=ny<m:
                if lst[nx][ny]==0 and (nx,ny) not in inq:
                    q.append((nx,ny,step+1))
                    inq.add((nx,ny))
    return -1

n,m=[int(x) for x in input().split()]
lst=[]
for _ in range(n):
    lst.append([int(x) for x in input().split()])
direction=[(0,1),(1,0),(-1,0),(0,-1)]
print(bfs(0,0))