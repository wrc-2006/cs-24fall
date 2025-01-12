'''
dfs超时，改成dijkstra
#pylint:skip-file
def dfs(x1,y1,x2,y2,cnt):
    global ans
    if cnt>ans:
        return ans
    visited[x1][y1]=True
    for a,b in d:
        nx,ny=x1+a,y1+b
        if nx==x2 and ny==y2:
            ans=min(ans,cnt+abs(int(lst[nx][ny])-int(lst[x1][y1])))
        if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
            if lst[nx][ny]!='#':
                dfs(nx,ny,x2,y2,cnt+abs(int(lst[nx][ny])-int(lst[x1][y1])))
    visited[x1][y1]=False

m,n,p=[int(x) for x in input().split()]
lst=[]
d=[(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(m):
    lst.append([x for x in input().split()])  ##字符串型
for _ in range(p):
    x1,y1,x2,y2=[int(x) for x in input().split()]
    ans=float('inf')
    visited=[[False]*n for i in range(m)]
    if lst[x1][y1]=='#' or lst[x2][y2]=='#':
        print('NO')
        continue
    dfs(x1,y1,x2,y2,0)
    print('NO' if ans==float('inf') else ans)
'''
import heapq

def dijkstra(x1,y1,x2,y2,lst):
    pq=[(0,(x1,y1))]
    distance=[[float('inf')]*n for _ in range(m)]
    distance[x1][y1]=0
    visited=set()
    while pq:
        dist,(x,y)=heapq.heappop(pq)
        if x==x2 and y==y2:
            return dist
        if (x,y) in visited:
            continue
        visited.add((x,y))
        for a,b in d:
            nx,ny=x+a,y+b
            if 0<=nx<m and 0<=ny<n:
                if (nx,ny) not in visited and lst[nx][ny]!='#':
                    newdist=dist+abs(int(lst[nx][ny])-int(lst[x][y]))
                    if newdist<distance[nx][ny]:
                        distance[nx][ny]=newdist
                        heapq.heappush(pq,(newdist,(nx,ny)))
    return 'NO'       
     
m,n,p=[int(x) for x in input().split()]
lst=[]
d=[(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(m):
    lst.append([x for x in input().split()])  ##字符串型
for _ in range(p):
    x1,y1,x2,y2=[int(x) for x in input().split()]
    if lst[x1][y1]=='#' or lst[x2][y2]=='#':
        print('NO')
        continue
    ans=dijkstra(x1,y1,x2,y2,lst)
    print(ans)