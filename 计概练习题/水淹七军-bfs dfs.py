'''
本题中等高没有淹没
oj上这题数据输入不标准，使用sys.stdin.read()一次性读取所有输入数据
'''
#pylint:skip-file
import sys
sys.setrecursionlimit(1<<30)
input=sys.stdin.read
data=input().split()
k=int(data[0])
data=data[1:]
def dfs(x,y,tx,ty):
    global ans
    if x==i-1 and y==j-1:
        ans=True
        return
    direction=[(0,1),(0,-1),(1,0),(-1,0)]
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<m and 0<=ny<n and height[nx][ny]<height[tx][ty]:
            height[nx][ny]=height[x][y]
            dfs(nx,ny,tx,ty)
    
for _ in range(k):
    m,n=int(data[0]),int(data[1])
    data=data[2:]
    height=[]
    for i in range(m):
        height.append(list(map(int,data[:n])))
        data=data[n:]
    i,j,p=map(int,data[:3])
    data=data[3:]
    water=[]
    ans=False
    for __ in range(p):
        water.append((int(data[0])-1,int(data[1])-1))
        data=data[2:]
    for q in water:
        dfs(q[0],q[1],q[0],q[1])
    print('Yes' if ans else 'No')
    
'''
这里的dfs不需要回溯
'''
#pylint:skip-file
import sys
sys.setrecursionlimit(1<<30)
input=sys.stdin.read
data=input().split()
k=int(data[0])
data=data[1:]

def dfs(x,y,tx,ty,rvisited):
    global ans
    if x==i-1 and y==j-1:
        ans=True
        return
    direction=[(0,1),(0,-1),(1,0),(-1,0)]
    rvisited[x][y]=True
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<m and 0<=ny<n and not rvisited[nx][ny] and height[nx][ny]<height[tx][ty]:
            dfs(nx,ny,tx,ty,rvisited)
    
for _ in range(k):
    m,n=int(data[0]),int(data[1])
    data=data[2:]
    height=[]
    for i in range(m):
        height.append(list(map(int,data[:n])))
        data=data[n:]
    i,j,p=map(int,data[:3])
    data=data[3:]
    water=[]
    ans=False
    rvisited=[[False]*n for ___ in range(m)]
    for __ in range(p):
        water.append((int(data[0])-1,int(data[1])-1))
        data=data[2:]
    for q in water:
        dfs(q[0],q[1],q[0],q[1],rvisited)
    print('Yes' if ans else 'No')



