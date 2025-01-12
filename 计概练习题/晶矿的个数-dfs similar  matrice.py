def dfs(x,y,color):
    lst[x][y]='#'
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<n and lst[nx][ny]==color:
            dfs(nx,ny,color)
    

k=int(input())
for _ in range(k):
    n=int(input())
    lst=[list(input()) for __ in range(n)]
    direction=[(1,0),(-1,0),(0,1),(0,-1)]
    red,black=0,0
    for i in range(n):
        for j in range(n):
            if lst[i][j]=='r':
                red+=1
                dfs(i,j,'r')
            if lst[i][j]=='b':
                black+=1
                dfs(i,j,'b')
    print(red,black)

