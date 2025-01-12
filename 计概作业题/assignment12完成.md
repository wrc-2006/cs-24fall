# Assignment #C: 五味杂陈 

Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：



代码：

```python
while True:
    a,b=[int(x) for x in input().split()]
    if a==b==0:
        break
    cnt=1
    a,b=max(a,b),min(a,b)
    while a/b<2 and a!=b:
        cnt+=1
        a,b=b,a-b
    if cnt%2==0:
        print('lose')
    else:
        print('win')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241210164707934](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241210164707934.png)



### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：和螺旋矩阵很像，但计算每圈总和时左上角一个数总是多算一次，但我那被转晕的脑袋已经想不出怎么改写程序了，一怒之下直接把第一个数改为0避免多算

我的代码真是毫无美感可言……

代码：

```python
from math import ceil
n=int(input())
lst=[]
for _ in range(n):
    lst.append([int(x) for x in input().split()])
d=[(0,1),(1,0),(0,-1),(-1,0)]
ans=0
for i in range(ceil(n/2)):
    cnt=0
    newans=lst[i][i]
    lst[i][i]=0
    x,y=i,i
    while cnt!=4:
        num=1
        a,b=d[cnt]
        while num<n-i*2:
            x+=a
            y+=b
            newans+=lst[x][y]
            num+=1
        cnt+=1
    ans=max(ans,newans)
print(ans)
    
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241210171633163](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241210171633163.png)



### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：



代码：

```python
n=int(input())
potion=[int(x) for x in input().split()]
health=0
positive=0
negative=[]
for i in potion:
    if i>=0:
        positive+=1
        health+=i
    else:
        negative.append(i)
        health+=i
        if health<0:
            health-=min(negative)
            negative.remove(min(negative))
print(positive+len(negative))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241211171602410](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241211171602410.png)



### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：



代码：

```python
pig=[]
ans=[]
while True:
    try:
        s=input()
        if len(s)>4:
            n=int(s[5:])
            pig.append(n)
            if not ans:
                ans.append(n)
            else:
                ans.append(min(n,ans[-1]))
        if s=='pop':
            if len(pig)>0:
                pig.pop()
                ans.pop()
        if s=='min':
            if len(pig)>0:
                print(ans[-1])
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241212160207313](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241212160207313.png)



### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：dfs超时了，dijkstra还不是很熟，照着模板大概抄出来的



代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241213134536104](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241213134536104.png)



### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：一开始把题目意思理解错了，对于当前时间是否是k的倍数少加了1



代码：

```python
from collections import deque
def bfs(x1,y1,x2,y2):
    inq=set()
    inq.add((x1,y1,0))
    q=deque([(x1,y1,0)])
    d=[(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        x,y,time=q.popleft()
        for a,b in d:
            nx,ny=x+a,y+b
            if nx==x2 and ny==y2:
                return time+1
            if 0<=nx<r and 0<=ny<c:
                if (time+1)%k!=0:
                    if (nx,ny,(time+1)%k) not in inq and lst[nx][ny]!='#':
                        inq.add((nx,ny,(time+1)%k))
                        q.append((nx,ny,time+1))
                else:
                    if (nx,ny,time%k) not in inq:
                        q.append((nx,ny,time+1))
                        inq.add((nx,ny,(time+1)%k))
                        

for _ in range(int(input())):
    r,c,k=[int(x) for x in input().split()]
    lst=[]
    for __ in range(r):
        lst.append(input())
    for i in range(r):
        if 'S' in lst[i]:
            x1,y1=i,lst[i].index('S')
        if 'E' in lst[i]:
            x2,y2=i,lst[i].index('E')
    ans=bfs(x1,y1,x2,y2)
    if ans==None:
        print('Oop!')
    else:
        print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241212173401007](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241212173401007.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

期末别寄期末别寄求求了，明天还要考四级，期末还有一堆考试ddl



