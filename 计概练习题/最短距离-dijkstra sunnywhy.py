import heapq

def dijkstra(n,s,t):
    graph=[[] for _ in range(n)]
    for u,v,w in lst:
        graph[u].append((v,w))
        graph[v].append((u,w))
    pq=[(0,s)]   #(distance,node)
    visited=set()
    distance=[float('inf')]*n
    distance[s]=0
    while pq:
        dist,node=heapq.heappop(pq)
        if node==t:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor,weight in graph[node]:
            if neighbor not in visited:
                newdist=dist+weight
                if newdist<distance[neighbor]:
                    distance[neighbor]=newdist
                    heapq.heappush(pq,(newdist,neighbor))
    return -1

n,m,s,t=[int(x) for  x in input().split()]
lst=[]
for _ in range(m):
    lst.append([int(x) for x in input().split()])
print(dijkstra(n, s, t))    
