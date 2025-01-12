import heapq
def dijkstra(s,end):
    graph=[[] for _ in range(n)]
    for u,v,w in lst:
        graph[u].append((v,w))
        graph[v].append((u,w))
    inq=set()
    q=[(0,s)]
    distance=[float('inf')]*n
    distance[s]=0
    while q:
        dist,node=heapq.heappop(q)
        if node==end:
            return dist
        if node not in inq:
            inq.add(node)
            for neighbor,weight in graph[node]:
                if neighbor not in inq:
                    newdist=dist+weight
                    if newdist<distance[neighbor]:
                        distance[neighbor]=newdist
                        heapq.heappush(q,(newdist,neighbor))
    return -1
    

n,m,s=[int(x) for x in input().split()]
lst=[]
for _ in range(m):
    lst.append([int(x) for x in input().split()])
ans=[]
for i in range(n):
    ans.append(dijkstra(s,i))
print(*ans)



