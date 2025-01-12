# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==同学的姓名、院系==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：



##### 代码

```python
# 
for i in range(5):
    s=[int(x) for x in input().split()]
    if 1 in s:
        row=i
        a=s.index(1)
print(abs(2-a)+abs(2-row))

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240924151928458](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240924151928458.png)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：



##### 代码

```python
# 
t=int(input())
for i in range(t):
    a,b=[int(x) for x in input().split()]
    if a%b==0:
        print(0)
    else:
        print(b-a%b)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240924161435707](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240924161435707.png)



### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：



##### 代码

```python
# 
n=int(input())
s=[int(x) for x in input().split()]
sum=0
officer=0
for i in s:
    if i>0:
        officer+=i
    elif i <0 and officer==0:
        sum+=1
    else:
        officer-=1 
print(sum)
         

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924161644897](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240924161644897.png)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：



##### 代码

```python
# 
l,m=map(int,input().split())
lst=[1]*(l+1)
for _ in range(m):
    p,q=[int(x) for x in input().split()]
    for i in range(p,q+1):
        lst[i]=0
print(lst.count(1))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924163312942](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240924163312942.png)



### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：



##### 代码

```python
#
a,b=map(int,input().split())
lst=[]
for i in range(a,b+1):
    bai_wei=i//100
    shi_wei=(i-i//100*100)//10
    ge_wei=i-bai_wei*100-shi_wei*10
    if bai_wei**3+shi_wei**3+ge_wei**3==i:
        lst.append(i)
if lst==[]:
    print('NO')
else:
    print(*lst)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240924170230105](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240924170230105.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：



##### 代码

```python
# 
import math
while True:
    n=int(input())
    if n==0:
        break
    lst=[]
    for _ in range(n):
        v,t=[int(x) for x in input().split()]
        if t<0:
            continue
        time=math.ceil((4.5/v)*3600)+t
        lst.append(time)
    print(min(lst))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240925205158990](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20240925205158990.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

之前为了能快点做题，从B站上找了些教程直接倍速，这周才开始真正看书学习。不看不知道，一看发现我还有这么多不知道或者在B站上看过却忘了，哎。每日选做里800的题基本都做完了，现在在补900，但是900的题有些我拿到手就没有思路了，呜呜呜看来是我数学差劲了。另外每日选做我才做到9月7号，争取在国庆期间赶上进度吧。



  
