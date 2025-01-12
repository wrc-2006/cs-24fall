# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：



代码：

```python
n=0
while True:
    p,e,i,d=[int(x) for x in input().split()]
    n+=1
    if p<0:
        break
    for j in range(1,1000):
        day=p+23*j
        if (day-e)%28==0 and (day-i)%33==0:
            break
    print(f'Case {n}: the next triple peak occurs in {day-d} days.')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241022151710617](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241022151710617.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：



代码：

```python
p=int(input())
value=sorted([int(x) for x in input().split()])
i,j=0,len(value)-1
mine,enermy=0,0
ans=0
while i<=j:
    if p<value[i]:
        if mine==enermy:
            ans=max(0,ans)
            break
        else:
            ans=max(ans,mine-enermy)
            p+=value[j]
            j-=1
            enermy+=1
    else:
        p-=value[i]
        i+=1
        mine+=1
        ans=max(ans,mine-enermy)
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241022153401892](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241022153401892.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：



代码：

```python
n=int(input())
t=[int(x) for x in input().split()]
lst=[]
for i,time in enumerate(t,1):
    lst.append([time,i])
lst.sort()
for i in lst:
    print(i[1],end=' ')
print()
waiting=0
m=1
for i in lst[:-1]:
    waiting+=i[0]*(n-m)
    m+=1
print(f'{waiting/n:.2f}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241022165520664](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241022165520664.png)



### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：本来一直WA，试的数据也都正确，翻群聊天记录时才看到之前有人说总日期整除260时会让年份多一



代码：

```python
n=int(input())
print(n)
lst_hmonth=['pop','no','zip','zotz','tzec','xul','yoxkin','mol','chen','yax','zac','ceh','mac','kankin','muan','pax','koyab','cumhu']
lst_t2=['imix','ik','akbal','kan','chicchan','cimi','manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib','caban','eznab','canac','ahau']
lst_t1=[x for x in range(1,14)]
for _ in range(n):
    hday,hmonth,hyear=[x for x in input().split()]
    hday=int(hday[:-1])
    hyear=int(hyear)
    if hmonth=='uayet':
        day=360+hday+1+365*hyear
    else:
        day=20*lst_hmonth.index(hmonth)+hday+1+365*hyear
    tyear=day//260
    if day%260==0:
        tyear-=1
    day%=260
    tday2=lst_t2[day%20-1]
    tday1=lst_t1[day%13-1]
    print(f'{tday1} {tday2} {tyear}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241022225925423](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241022225925423.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：



代码：

```python
n=int(input())
lst=[]
for _ in range(n):
    x,h=map(int,input().split())
    lst.append([x,h])
ans=min(n,2)
for i in range(1,n-1):
    if lst[i][1]<lst[i][0]-lst[i-1][0]:
        ans+=1
        continue
    elif lst[i][1]<lst[i+1][0]-lst[i][0]:
        ans+=1
        lst[i][0]+=lst[i][1]
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241023192635535](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241023192635535.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：睡一觉起来之后才搞完了这道题，在仔细对比答案与我的代码后，发现雷达的坐标不一定是整数，我把雷达覆盖范围用int取整了啊啊啊



代码：

```python
from math import sqrt
case=0
while True:
    n,d=[int(x) for x in input().split()]
    if n==d==0:
        break
    case+=1
    ans=1
    radar=[]
    for _ in range(n):
        x,y=[int(x) for x in input().split()]
        if y>d:
            ans=-1
        else:
            m=sqrt(d*d-y*y)
            radar.append([x-m,x+m])
    radar.sort()
    if ans==-1:
        print(f'Case {case}: {ans}')
    else:
        rst,red=radar[0][0],radar[0][1]
        for st,ed in radar[1:]:
            if st>red:
                ans+=1
                rst,red=st,ed
            else:
                rst,red=st,min(ed,red)
        print(f'Case {case}: {ans}')
    input()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241024090650156](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241024090650156.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

最近这段时间在计概上花的时间比较少，而且也明显感觉到现在每日选做的难度上来了，很多题拿到手根本没有思路，尤其是贪心，每道题的解题思路之间似乎都没有什么非常鲜明的共同点，如果拿到题能差不多想出思路来，那基本就没什么问题，但要是想不出来，以我的水平，可能苦想几个小时也想不到解题方向。



