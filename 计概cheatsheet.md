# **背包dp**

## 0-1背包

小偷背包：

```python
n,b=[int(x) for x in input().split()]  #n物品数 b最大承重
price=[int(x) for x in input().split()]
weight=[int(x) for x in input().split()]
dp=[0]*(b+1)   #用于存储不同重量下的最大价值
for i in range(n):
    for j in range(b,weight[i]-1,-1):
        dp[j]=max(dp[j],dp[j-weight[i]]+price[i])
print(dp[-1])
```

或用二维数组

```python
n,b=[int(x) for x in input().split()]
price=[int(x) for x in input().split()]
weight=[int(x) for x in input().split()]
cell=[[0 for i in range(b+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,b+1):
        if j>=weight[i-1]:
            cell[i][j]=max(cell[i-1][j],cell[i-1][j-weight[i-1]]+price[i-1])
        else:
            cell[i][j]=cell[i-1][j]
print(cell[n][b])
```

## 完全背包

将0-1背包中内层循环改为正着遍历即可（这里其实就利用了先前已经得到的信息来简化转移：在先前的转移中物品i可能已经用过若干次了）

cut ribbon剪彩

```python
n,a,b,c=[int(x) for x in input().split()]
s=[a,b,c]
dp=[0]+[-float('inf')]*n
for i in range(1,n+1):
    for j in s:
        if i>=j:
            dp[i]=max(dp[i],dp[i-j]+1)
print(dp[n])
```

零钱兑换

```python
n,m=[int(x) for x in input().split()]  #n零钱种类数 m总金额
coin=[int(x) for x in input().split()]
dp=[0]+[float('inf')]*m
for i in range(1,m+1):
    for j in coin:
        if j<=i:
            dp[i]=min(dp[i-j]+1,dp[i])
if dp[m]==float('inf'):
    print(-1)
else:
    print(dp[m])
```

允许在不超内存的情况下无限提取（不需要装满）

```python
def knapsack_complete(weights, values, capacity):
    dp = [0] * (capacity + 1)  # dp[j]为当背包容量为j时,背包所能容纳的最大价值
    dp[0] = 0
    for i in range(len(weights)):  # 遍历所有物品
        for j in range(weights[i], capacity + 1):  # 从当前物品的重量开始，计算每个容量的最大价值
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[capacity]
```

## 多重背包

把「每种物品选k次」等价转换为「有k个相同的物品，每个物品选一次」。转换成了一个 0-1 背包模型

coins

```python

```

### DFS 

oj上compile error时在前面加#pylint:skip-file

寻找所有最优解时需要回溯，寻找某一特定道路时不需要回溯

lake counting

```python
import sys
sys.setrecursionlimit(1<<20)
def dfs(x,y):
    direction=[(1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,0),(-1,1),(-1,-1)]
    field[x][y]='.'
    for a,b in direction:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m and field[nx][ny]=='W':
            dfs(nx,ny)
n,m=map(int,input().split())
field=[list(input()) for _ in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if field[i][j]=='W':
            ans+=1
            dfs(i,j)
print(ans)
```

两座孤岛最短距离

bfs中需标记已访问过的路径，标记之后不用多源bfs也能ac

```python
from collections import deque
def dfs(x,y,island):
    lst[x][y]=2
    for a,b in d:
        nx,ny=x+a,y+b
        if 0<=nx<n and 0<=ny<m:
            if lst[nx][ny]==1:
                dfs(nx,ny,island)
            if lst[nx][ny]==0:
                island.append((x,y,0))           
def bfs(q): 
    while q:
        for _ in range(len(q)):
            x,y,step=q.popleft()
            for a,b in d:
                nx,ny=x+a,y+b
                if 0<=nx<n and 0<=ny<m:
                    if lst[nx][ny]==1:
                        return step
                    if lst[nx][ny]==0:
                        lst[nx][ny]=2
                        q.append((nx,ny,step+1))               
lst=[]
n=int(input())
for _ in range(n):
    lst.append([int(x) for x in input()])
m=len(lst[0])
d=[(0,1),(1,0),(-1,0),(0,-1)]
q=deque()
for i in range(n):
    for j in range(m):
        if lst[i][j]==1:
            dfs(i,j,q)
            newans=bfs(q)
            break
    else:
        continue
    break     
print(newans)
```

螃蟹采蘑菇

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

水淹七军

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
#这里的dfs不需要回溯
```

### BFS

螃蟹采蘑菇

```python
from collections import deque
def bfs(x1,y1,x2,y2):
    inq=set((x1,y1))
    inq.add((x2,y2))
    q=deque([(x1,y1,x2,y2)])
    while q:
        x1,y1,x2,y2=q.popleft()
        if lst[x1][y1]==9 or lst[x2][y2]==9:
            return 'yes'
        for a,b in d:
            nx1,ny1,nx2,ny2=x1+a,y1+b,x2+a,y2+b
            if 0<=nx1<n and 0<=nx2<n and 0<=ny1<n and 0<=ny2<n:
                if (nx1,ny1) not in inq or (nx2,ny2) not in inq:
                    if lst[nx1][ny1]!=1 and lst[nx2][ny2]!=1:
                        inq.add((nx1,ny1))
                        inq.add((nx2,ny2))
                        q.append((nx1,ny1,nx2,ny2))
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
print(bfs(x1,y1,x2,y2))
```

### Dijkstra

最短路径 无向图

```python
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
```

走山路

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

### T-primes  欧拉筛

```python
def is_prime(n):
    lst=[True]*(n+1)
    primes=[]
    lst[1]=False
    for i in range(2,n+1):
        if lst[i]:
            primes.append(i)
        for p in primes:
            if i*p>n:
                break
            lst[i*p]=False
            if i%p==0:
                break
    return lst
n=int(input())
x=[int(x) for x in input().split()]
lst=is_prime(1000000)
for i in x:
    sqrt_i=i**0.5
    if (sqrt_i)%1==0:
        if lst[int(sqrt_i)]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
```

```python
n = int(input())
isPrime = [True]*(n+1)
for i in range(2, n+1):
    if isPrime[i]:
        for j in range(2*i,n+1,i):
            isPrime[j] = False
```

### 拦截导弹

```python
k=int(input())
height=[int(x) for x in input().split()]
dp=[1]*k
for i in range(1,k):
    for j in range(i):
        if height[j]>=height[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
```

### 登山

```python
n=int(input())
h=[0]+[int(x) for x in input().split()]
dp1=[0]*(n+1)   #dp1[i]:i前（不包括i）最大上升
dp2=[1]*(n+1)   #dp2[i]:i后（包括i）最大下降
for i in range(2,n+1):
    for j in range(1,i):
        if h[j]<h[i]:
            dp1[i]=max(dp1[i],dp1[j]+1)
for i in range(n,1,-1):
    for j in range(i+1,n+1):    ##或range(n,i,-1)也行
        if h[j]<h[i]:
            dp2[i]=max(dp2[i],dp2[j]+1)
ans=[0]*(n+1)
for i in range(n+1):
    ans[i]=dp1[i]+dp2[i]
print(max(ans))
```

### 最长公共子序列

```python
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    lcs_length = dp[m][n] # 最长公共子序列的长度
    lcs = [] # 回溯以构建最长公共子序列
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs.reverse() # 因为我们是从后往前添加元素到列表中的，所以我们需要反转它
    return ''.join(lcs), lcs_length
```

### 快速堆猪 辅助栈

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
                ans.append(min(n,ans[-1]))    ##加入n和最后一个数当中较小的一个
        if s=='pop':                    ##ans中猪的数量与pig中一致，也使最后一个为最小值
            if len(pig)>0:
                pig.pop()
                ans.pop()
        if s=='min':
            if len(pig)>0:
                print(ans[-1])
    except EOFError:
        break
```

### 滑雪

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

### 全排列

```python
def permutation(s):
    ans=[]
    if len(s)==0:
        return [[]]
    for i in range(len(s)):
        current=s[i]
        remain=s[:i]+s[i+1:]
        repermutation=permutation(remain)
        for a in repermutation:
            ans.append([current]+a)
    return ans
n=int(input())
s=[int(x) for x in range(1,n+1)]
ans=permutation(s)
for i in ans:
    print(*i)
```

### 最大最小整数

```python
n=int(input())
s=[x for x in input().split()]
maxn,minn='',''
s.sort(reverse=True)
while True:
    exchange=0
    for i in range(len(s)-1):
        if s[i+1] in s[i]:
            if s[i+1]+s[i]>s[i]+s[i+1]:
                s[i],s[i+1]=s[i+1],s[i]
                exchange+=1
    if exchange==0:
        break    
for i in s:
    maxn+=i
s.reverse()
for i in s:
    minn+=i
print(int(maxn),int(minn))
```

### 最大整数

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

### two point

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = left = pre_max = suf_max = 0  # 初始化结果、左指针和两个最大高度为0
        right = len(height) - 1  # 初始化右指针为数组末尾
        while left < right:  # 当左指针小于右指针时循环
            pre_max = max(pre_max, height[left])  # 更新左指针位置的最大高度
            suf_max = max(suf_max, height[right])  # 更新右指针位置的最大高度
            if pre_max < suf_max:  # 如果左指针位置的最大高度小于右指针位置的最大高度
                ans += pre_max - height[left]  # 计算并累加左指针位置能够接住的雨水量
                left += 1  # 移动左指针
            else:  # 否则
                ans += suf_max - height[right]  # 计算并累加右指针位置能够接住的雨水量
                right -= 1  # 移动右指针
        return ans  # 返回最终结果
```

河中跳房子

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

### 单调栈

```python
#比它大的数在几位数后出现
p=list(map(int,input().split()))
index=[0]*len(p)
stack=[]
for i in range(len(p)-1,-1,-1):
    t=p[i]
    while stack and t>p[stack[-1]]:
        stack.pop()
    if stack:
        index[i]=stack[-1]-i
    stack.append(i)
print(index)
```

### 杂七杂八

·hex(x) oct(x) bin(x) 将一个整数x转换为一个十六进制、八进制、二进制的字符串并且有‘0x’ ‘0o’ ‘0b’前缀

·math.factorial()可计算阶乘

·math.ceil向上取整

·ord（） chr（）

![image-20241225211113876](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241225211113876.png)

```python
import bisect
 a = [1, 2, 4, 4, 8]
 print(bisect.bisect_left(a, 4))  # 输出: 2
 print(bisect.bisect_right(a, 4))  # 输出: 4
 print(bisect.bisect(a, 4))  # 输出: 4  同bisect_right
```

·lst.insert（index，object）

```python
char.isupper()  
char.islower()  #返回True/False
str.lower():    #将字符串中的所有大写字母转换为小写。
str.upper():    #将字符串中的所有小写字母转换为大写。
str.capitalize(): #将字符串的第一个字母转换为大写，其余字母转换为小写。
str.title(): #将字符串中每个单词的第一个字母转换为大写，其余字母转换为小写。
str.swapcase(): #将字符串中所有的大写字母转换为小写，同时将所有的小写字母转换为大写。
```

```python
import heapq
 data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
 heapq.heapify(data)
 print(data)  # 输出: [0, 1, 2, 3, 9, 5, 4, 6, 8, 7]
 heapq.heappush(data, -5)
 print(data)  # 输出: [-5, 0, 2, 3, 1, 5, 4, 6, 8, 7, 9]
 print(heapq.heappop(data))  # 输出: -5
```

