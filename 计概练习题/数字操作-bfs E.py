from collections import deque
def bfs(n):
    inq=set()
    inq.add(1)
    q=deque()
    q.append((1,0))
    while q:
        front,step=q.popleft()
        if front==n:
            return step
        if front*2<=n and front*2 not in inq:
            inq.add(front*2)
            q.append((front*2,step+1))
        if front+1<=n and front+1 not in inq:
            inq.add(front+1)
            q.append((front+1,step+1))
            
print(bfs(int(input())))
    