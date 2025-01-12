# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：



代码：

```python
n,m=[int(x) for x in input().split()]
lst=[[0]*(m+2)]
for _ in range(n):
    s=[int(x) for x in input().split()]
    lst.append([0]+s+[0])
lst.append([0]*(m+2))
ans=0
for i in range(n+2):
    for j in range(m+2):
        if lst[i][j]==1:
            ans+=4-lst[i-1][j]-lst[i+1][j]-lst[i][j+1]-lst[i][j-1]
print(ans) 
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241113101230942](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241113101230942.png)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：

我还不会用类……leetcode答案还看不懂……好多东西要补……

完蛋辣，好不容易把代码写出来结果发现leetcode上要遵循一定格式（我还不会啊啊啊）（我可以写OJ上的题吗……）

代码：

```python
k=int(input())
arr=[[0]*k for i in range(k)]
lst=[[1000]*(k+2)]+[[1000]+i+[1000] for i in arr]+[[1000]*(k+2)]
i,j=1,1
direction=[[0,1],[1,0],[0,-1],[-1,0]]
index=0
dire=direction[0]
m,n=dire
num=1
while num<=k**2:
    if lst[i][j]<1000:
        arr[i-1][j-1]=num
        num+=1
        lst[i][j]=1000
        i+=m
        j+=n
    else:
        index=(index+1)%4
        dire=direction[index]
        i-=m
        j-=n
        m,n=dire
        i+=m
        j+=n
for i in arr:
    print(*i)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241113214135411](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241113214135411.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：



代码：

```python
d=int(input())
n=int(input())
lst=[[0]*1025 for i in range(1025)]
for _ in range(n):
    x,y,i=[int(x) for x in input().split()]
    for p in range(max(0,x-d),min(1025,x+d+1)):
        for q in range(max(0,y-d),min(1025,y+d+1)):
            lst[p][q]+=i
ans,cnt=0,1
for i in range(0,1025):
    for j in range(0,1025):
        if lst[i][j]>ans:
            ans=lst[i][j]
            cnt=1
        elif lst[i][j]==ans:
            cnt+=1
print(cnt,ans)
    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241114155110384](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241114155110384.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：



代码：

```python
n=int(input())
lst=[int(x) for x in input().split()]
if n>=2:
    newlst=[lst[i]-lst[i-1] for i in range(1,n)]
else:
    newlst=[0]
for i in newlst:
    if i!=0:
        check=i
        break
else:
    check=0
ans=[1,2][check!=0]
for i in newlst:
    if i*check<0:
        ans+=1
        check=i
print(ans)
    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241115135852692](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241115135852692.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：好像一直把题目理解错了，我以为ak是指列表中的第k个元素www还在考虑会不会超出列表索引范围www



代码：

```python
n=int(input())
a=[int(x) for x in input().split()]
cnt=[0]*100001
for i in a:
    cnt[i]+=1
dp=[0]*100001
dp[1]=cnt[1]
for i in range(1,100001):
    dp[i]=max(dp[i-1],dp[i-2]+i*cnt[i])
print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241115224800399](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241115224800399.png)



### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：一次一次试，终于让我试出来www



代码：

```python
while True:
    n=int(input())
    if n==0:
        break
    ans=0
    tian=sorted([int(x) for x in input().split()],reverse=True)
    king=sorted([int(x) for x in input().split()],reverse=True)
    while tian:
        if tian[0]>king[0]:
            ans+=1
            del tian[0]
            del king[0]
        else:
            if tian[-1]>king[-1]:
                ans+=1
                del tian[-1]
                del king[-1]
            elif tian[-1]<king[0]:
                ans-=1
                del tian[-1]
                del king[0]
            else:
                del tian[-1]
                del king[0]
                
    print(200*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241115163051411](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241115163051411.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

期中周刚刚结束……还有好多好多东西要补……recursion都还不熟……



