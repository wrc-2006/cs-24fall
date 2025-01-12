# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）⽉考： AC6<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：这题考试时一直超时www搞了近一个小时才AC



代码：

```python
a=[int(x) for x in input().split()]
dp=[0]*(len(a))
dp[-1]=a[-1]
for i in range(len(a)-2,-1,-1):
    dp[i]=max(dp[i+1],a[i])
ans=0
for i in range(len(a)-1):
    ans=max(ans,dp[i]-a[i])
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241207221946370](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241207221946370.png)



### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：自己想不出思路，问了ai才有大概思路



代码：

```python
n,k=[int(x) for x in input().split()]
t=[int(x) for x in input().split()]
t.sort(reverse=True)
maxt=sum(t)/k
cnt=1
for i in range(len(t)):
    if t[i]>maxt:
        maxt=sum(t[i+1:])/(k-cnt)
        cnt+=1
print(f'{maxt:.3f}')
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241208131620959](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241208131620959.png)



### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：使用暴力解题超时了，dp的状态转移方程自己想还是想不出来，甚至看完答案后还是感觉不太能理解



代码：

```python
p=[int(x) for x in input().split(',')]
dp1,dp2=[0]*len(p),[0]*len(p)
dp1[0]=dp2[0]=p[0]
for i in range(1,len(p)):
    dp1[i]=max(p[i],dp1[i-1]+p[i])
    dp2[i]=max(p[i],dp1[i-1],dp2[i-1]+p[i])
print(max(dp2))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241208145632138](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241208145632138.png)



### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：优惠券只能用一张！！！www



代码：

```python
def dfs(p,discount,selected):
    global ans,cost
    if selected==n:
        sumcost=sum(cost)
        cnt=sumcost//300
        rcost=cost[:]
        for i in range(m):
            for shopdiscount in discount[i][::-1]:
                if rcost[i]>=shopdiscount[0]:
                    sumcost-=shopdiscount[1]
                    break
                
        ans=min(ans,int(sumcost-50*cnt))
        return
    for shop,price in p[selected]:
        cost[shop-1]+=price
        dfs(p,discount,selected+1)
        cost[shop-1]-=price
    
n,m=[int(x) for x in input().split()]
p=[[]for _ in range(n)]
discount=[[]for _ in range(m)]
for _ in range(n):
    s=[x for x in input().split()]
    p[_]=[list(map(int,x.split(':'))) for x in s]   #商店，价格
for _ in range(m):
    s=[x for x in input().split()]
    discount[_]=[list(map(int,x.split('-'))) for x in s]  #满减
    discount[_].sort(key=lambda x:x[1])
ans=float('inf')
selected=0
cost=[0 for i in range(m)]
dfs(p,discount,0)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241208204429028](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241208204429028.png)



### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：考试时用dfs来找孤岛位置，再用bfs求距离，结果超时了www

现在改成两个bfs还是一直超时，哎

看一下群聊，好像得直接找出边界点，思考ing

为什么越改耗时越长了![1F628](C:\Users\lp\AppData\LocalLow\2345Pinyin\emoji\2018011201\1F628.png)

最终发现超时完全是因为bfs中没有标记已访问过的路径，标记之后好像不用多源bfs也能ac

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241209193050631](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241209193050631.png)



### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：怎么感觉做greedy题目完全凭感觉![1F628](C:\Users\lp\AppData\LocalLow\2345Pinyin\emoji\2018011201\1F628.png)

不知道为什么就随便试一试排列顺序就出来了ww

代码：

```python
n=int(input())
a,b=[int(x) for x in input().split()]
minister=[]
for i in range(n):
    minister.append([int(x) for x in input().split()])
minister.sort(key=lambda x:x[0]*x[1])
dp=[0]*n
dp[0]=a
ans=a//minister[0][1]
for i in range(1,n):
    dp[i]=dp[i-1]*minister[i-1][0]
    ans=max(ans,dp[i]//minister[i][1])
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241209200710612](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241209200710612.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

考得对期末完全没有信心了www

期末再这样数算就要润到其他班了www



