# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 10, 2024

2024 fall, Complied by ==同学的姓名、院系==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：



##### 代码

```python
# a=int(input())
if a%4!=0:
    print('N')
elif a%100==0 and a%400!=0:
    print('N')
else:
    print('Y')


```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240920103318060](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240920103318060.png)





### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：



##### 代码

```python
# a=int(input())
if a%2!=0:
    print('0 0')
elif a%4==0:
    m=a//4
    n=a//2
    print(m,n)
else:
    m=a//4+1
    n=a//2
    print(m,n)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240920101057359](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240920101057359.png)



### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：



##### 代码

```python
# M,N=map(int,input().split())
if (M*N)%2==0:
    print(M*N//2)
else:
    print((M*N-1)//2)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920101732641](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240920101732641.png)



### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：



##### 代码

```python
# import math
m,n,a=[int(x) for x in input().split()]
print(math.ceil(m/a)*math.ceil(n/a))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920101907812](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240920101907812.png)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：



##### 代码

```python
# m=input()
n=input()
if m.lower() > n.lower():
    print(1)
elif m.lower()<n.lower():
    print(-1)
else:
    print(0)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920101951125](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240920101951125.png)



### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：



##### 代码

```python
# n=int(input())
s=0
for i in range(n):
    a,b,c=map(int,input().split())
    if a+b+c==2 or a+b+c==3:
        s+=1
print(s)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920102034686](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240920102034686.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

作为一个电脑与编程零基础的小白，初看这些题目真的是万分惶恐，因为什么也看不懂，连最基础的print也不会。经过两周的速成，也终于能写出一些最简单的题目，不过略微上些难度还是能把我难倒。总体来说，已掌握一部分基础语法以及判断语句循环语句的用法（虽然还不太熟练）



