# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：



代码：

```python
def move(A,C):
    print(f'{A}->{C}')
def tower(n,A,B,C):
    if n==1:
        move(A,C)
    else:
        tower(n-1,A,C,B)
        move(A,C)
        tower(n-1,B,A,C)
n=int(input())
print(2**n-1)
A,B,C='A','B','C'
tower(n,A,B,C)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241030161251529](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241030161251529.png)



### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：



代码：

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



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241030165616261](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241030165616261.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路 ：



代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102212156992](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241102212156992.png)



### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：



代码：

```python
n,b=[int(x) for x in input().split()]
price=[int(x) for x in input().split()]
weight=[int(x) for x in input().split()]
dp=[0]*(b+1)
for i in range(n):
    for j in range(b,weight[i]-1,-1):
        dp[j]=max(dp[j],dp[j-weight[i]]+price[i])
print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102221419200](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241102221419200.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：没有思路，瞄了一眼答案说用全排列，然后自己把剩下的代码凑出来了呜呜呜



代码：

```python
def permutation(lst):
    ans=[]
    if len(lst)==0:
        return [[]]
    for i in range(len(lst)):
        current=lst[i]
        remain=lst[:i]+lst[i+1:]
        permutations=permutation(remain)
        for a in permutations:
            ans.append([current]+a)
    return ans
n=int(input())
lst=[1,2,3,4,5,6,7,8]
ans=permutation(lst)
newans=[]
for item in ans:
    for i in range(len(item)):
        for j in range(i+1,len(item)):
            if j-i==abs(item[i]-item[j]):
                
                break
        else:
            continue
        break
    else:
        newans.append(item)
newans.sort()
for _ in range(n):
    b=int(input())
    print(''.join(map(str,newans[b-1])))  
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102120018606](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241102120018606.png)



### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：



代码：

```python
n,a,b,c=[int(x) for x in input().split()]
s=[a,b,c]
dp=[0]+[-100000]*n
for i in range(1,n+1):
    for j in s:
        if i>=j:
            dp[i]=max(dp[i],dp[i-j]+1)
print(dp[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102230721694](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241102230721694.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

啊啊啊啊好难啊啊啊啊要疯啦啊啊啊不行啦





 
