def change(x,y,light):
    d=[(0,1),(1,0),(-1,0),(0,-1)]
    light[x][y]^=1
    ans[x][y]^=1
    for a,b in d:
        nx,ny=x+a,y+b
        if 0<=nx<5 and 0<=ny<6:
            light[nx][ny]^=1
def play():
    for j in range(1,6):
        for i in range(5):
            if light[i][j-1]==1:
                change(i,j,light)

light=[]
for _ in range(5):
    light.append([int(x) for x in input().split()])
ans=[[0]*6 for _ in range(5)]

play()
for i in range(5):
    if light[i][5]==1:
        change(i,0,light)
play()

for i in ans:
    print(*i)