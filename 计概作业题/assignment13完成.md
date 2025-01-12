# Assignment #D: 十全十美 

Updated 1254 GMT+8 Dec 17, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692

思路：



代码：

```python
n=int(input())
for _ in range(n):
    coin={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0}
    check={'A':False,'B':False,'C':False,'D':False,'E':False,'F':False,'G':False,'H':False,'I':False,'J':False,'K':False,'L':False}
    for __ in range(3):
        a,b,c=[x for x in input().split()]
        if c=='even':
            for i in a+b:
                check[i]=True
                coin[i]=0
        if c=='up':
            for i in a:
                if not check[i]:
                    coin[i]+=1
            for j in b:
                if not check[j]:
                    coin[j]-=1
        if c=='down':
            for i in a:
                if not check[i]:
                    coin[i]-=1
            for j in b:
                if not check[j]:
                    coin[j]+=1
    ans=[]
    for name,result in coin.items():
        if result!=0:
            ans.append([name,result])
    
    rename,re=ans[0][0],ans[0][1]
    for i in ans[1:]:
        if abs(i[1])>abs(re):
            rename,re=i[0],i[1]
    weigh=['light','heavy'][re>0]
    print(f'{rename} is the counterfeit coin and it is {weigh}.')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241220140733387](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241220140733387.png)



### 01088: 滑雪

dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：关于我把tag看成bfs，dfs similar于是用bfs写了半个多小时并且一直超时这件事www



代码：

```python
import sys
from functools import lru_cache
sys.setrecursionlimit(1<<30)
@lru_cache(maxsize=None)
def dfs(x,y):
    step=1
    for a,b in d:
        nx,ny=x+a,y+b
        if 0<=nx<r and 0<=ny<c and h[nx][ny]<h[x][y]:
            step=max(step,1+dfs(nx,ny))
    return step

r,c=[int(x) for x in input().split()]
h=[]
for _ in range(r):
    h.append([int(x) for x in input().split()])
d=[(0,1),(1,0),(-1,0),(0,-1)]
out=0
for i in range(r):
    for j in range(c):
        out=max(out,dfs(i,j))
print(out)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241217165142808](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241217165142808.png)



### 25572: 螃蟹采蘑菇

bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：



代码：

```python
def dfs(x1,y1,x2,y2,tx,ty):
    if (x1==tx and y1==ty) or (x2==tx and y2==ty):
        return 'yes'
    ans='no'
    visited[x1][y1]=True
    visited[x2][y2]=True
    for a,b in d:
        nx1,ny1,nx2,ny2=x1+a,y1+b,x2+a,y2+b
        if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0<=ny2<n:
            if lst[nx1][ny1]!=1 and lst[nx2][ny2]!=1:
                if (not visited[nx1][ny1]) or (not visited[nx2][ny2]):
                    ans=dfs(nx1,ny1,nx2,ny2,tx,ty)
                    if ans=='yes':
                        return ans
                    
    return 'no'

n=int(input())
lst=[]
position=[]
for _ in range(n):
    s=[int(x) for x in input().split()]
    lst.append(s)
    if 5 in s:
        position.append((_,s.index(5)))
        lst[_][s.index(5)]=0
    if 5 in s:
        position.append((_,s.index(5)))
        lst[_][s.index(5)]=0
    if 9 in s:
        tx,ty=_,s.index(9)
d=[(0,1),(1,0),(-1,0),(0,-1)]
x1,y1=position[0]
x2,y2=position[1]
visited=[[False]*n for i in range(n)]
print(dfs(x1,y1,x2,y2,tx,ty))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241217175046896](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241217175046896.png)



### 27373: 最大整数

dp, http://cs101.openjudge.cn/practice/27373/

思路：



代码：

```python
def check(x):
    if x=='':
        return 0
    else:
        return int(x)
    
m=int(input())
n=int(input())
s=[str(x) for x in input().split()]
s.sort(reverse=True)
while True:
    exchange=0
    for i in range(len(s)-1):
        if s[i+1] in s[i]:
            if s[i+1]+s[i]>s[i]+s[i+1]:
                s[i+1],s[i]=s[i],s[i+1]
                exchange+=1
    if exchange==0:
        break
dp=[['']*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if len(s[i-1])>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=str(max(check(dp[i-1][j]),int(dp[i-1][j-len(s[i-1])]+s[i-1])))
print(dp[n][m])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241220151944518](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241220151944518.png)



### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811

思路：好难，没有思路，看题解的



代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241220164108975](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241220164108975.png)



### 08210: 河中跳房子

binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：丸辣二分查找太久不用全忘辣，自己写的奇奇怪怪的程序还一直超时



代码：

```python
l,n,m=[int(x) for x in input().split()]
stone=[0]
for _ in range(n):
    stone.append(int(input()))
stone.append(l)
def check(x):
    num=0
    now=0
    for i in range(1,n+2):
        if stone[i]-now<x:
            num+=1
        else:
            now=stone[i]
    if num>m:
        return True
    else:
        return False
lo,hi=0,l+1
ans=0
while lo<hi:
    mid=(lo+hi)//2
    if check(mid):
        hi=mid
    else:
        lo=mid+1
        ans=mid
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241218213050301](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241218213050301.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

正在写往年机考题，还是对机考没有信心怎么办



