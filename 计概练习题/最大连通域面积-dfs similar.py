import sys
sys.setrecursionlimit(1<<30)

'''
def dfs(x,y):
    ans=1
    direction=[(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]
    field[x][y]='.'
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m and field[nx][ny]=='W':
            ans+=dfs(nx,ny)            
    return ans
递归
'''
'''
单调栈
'''
def dfs(x,y):
    ans=1
    stack=[(x,y)]
    direction=[(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]
    field[x][y]='.'
    while stack:
        x,y=stack.pop()
        for a,b in direction:
            nx,ny=x+a,y+b
            if 0<=nx<n and 0<=ny<m and field[nx][ny]=='W':
                ans+=1
                field[nx][ny]='.'
                stack.append((nx,ny))
    return ans
                        
    
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    field=[list(input()) for _ in range(n)]
    ans=0
    for i in range(n):
        for j in range(m):
            if field[i][j]=='W':
                ans=max(ans,dfs(i,j))
              
    print(ans)
