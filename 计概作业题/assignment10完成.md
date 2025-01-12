# Assignment #10: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：第一次用洛谷，AC之后竟然还有小烟花，好有仪式感的网站



代码：

```python
import sys
from functools import lru_cache
sys.setrecursionlimit(1<<30)
@lru_cache(maxsize=None)

def step(n):
    if dp[n]!=0:
        return dp[n]
    else:
        dp[n]=step(n-1)+step(n-2)
        return dp[n]

n=int(input())
dp=[0]*5001
dp[1],dp[2]=1,2
print(step(n))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241126135136288](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241126135136288.png)



### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：



代码：

```python
n=int(input())
dp=[0]*26
dp[1]=1
for i in range(2,26):
    dp[i]=sum(dp[:i])+1
print(dp[n])
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241126151644482](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241126151644482.png)



### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：一开始使用数学方法直接求解，还特地去问AIPython中是否有计算组合数的函数，结果超时了……然后按dp写时又因为没有每一步取模超内存了



代码：

```python
t,k=[int(x) for x in input().split()]
dp=[1]*100001
s=[1]*100001
for i in range(1,100001):   
    if i>=k:
        dp[i]=(dp[i-1]+dp[i-k])%1000000007
    s[i]=(s[i-1]+dp[i])%1000000007
for _ in range(t):
    a,b=[int(x) for x in input().split()]
    print((s[b]-s[a-1])%1000000007)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241128173009309](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241128173009309.png)



### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：



代码：

```python
dp=[[False]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                dp[i][j]=True
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
        ans=''
        for i in range(len(s)):
            for j in range(i,len(s)):
                if dp[i][j] and j-i+1>len(ans):
                    ans=s[i:j+1]
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241129143644197](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241129143644197.png)





### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：感觉我学不好了呜呜呜![image-20241129174900688](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241129174900688.png)



代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241129174832864](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241129174832864.png)



### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：一开始以为是求步数，代码很快就写了个大概，但运行时发现了许多千奇百怪的小bug，好不容易成功后发现题目要求的是线段数……

耗时一天……

代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241201174346948](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241201174346948.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

写前两道题时我是心高气傲

写后几道题时我是生死难料

感觉月考又要寄了





