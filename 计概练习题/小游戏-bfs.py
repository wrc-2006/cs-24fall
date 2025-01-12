'''
要求的是线段数而不是步数
'''
from collections import deque
def is_valid(x,y):
    if 0<=x<=(w+1) and 0<=y<=(h+1) and lst[y][x]!='X' and (x,y) not in inq:
        return True
    else:
        return False
def bfs(x1,y1,x2,y2):
    global inq
    direction=[(1,0),(-1,0),(0,1),(0,-1)]
    inq=set()
    inq.add((x1,y1))
    q=deque()
    q.append([x1,y1,0])
    while q:
        first,second,step=q.popleft()
        for a,b in direction:
            nx,ny=first,second
            while True:
                nx+=a
                ny+=b
                if nx==x2 and ny==y2:
                    return step+1
                if not is_valid(nx,ny):
                    break
                inq.add((nx,ny))
                q.append([nx,ny,step+1])
                    
cnt=0
while True:
    cnt+=1
    w,h=[int(x) for x in input().split()]
    if w==h==0:
        break
    lst,card=['.'*(w+2)],[]
    for _ in range(h):
        lst.append('.'+input()+'.')
    lst.append('.'*(w+2))
    while True:
        x1,y1,x2,y2=[int(x) for x in input().split()]
        if x1==0:
            break
        card.append([x1,y1,x2,y2])
    print(f'Board #{cnt}:')
    for i in range(1,len(card)+1):
        ans=bfs(card[i-1][0],card[i-1][1],card[i-1][2],card[i-1][3])
        if ans==None:
            print(f'Pair {i}: impossible.')
        else:
            print(f'Pair {i}: {ans} segments.')
    print()