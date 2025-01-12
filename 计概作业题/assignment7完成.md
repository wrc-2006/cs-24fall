# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）⽉考： AC6<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。

 

## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：



代码：

```python
n=int(input())
lst=[]
for i in range(n):
    num,age=[x for x in input().split()]
    lst.append([int(age),num])
newlst=sorted(lst,key=lambda x:(-x[0],lst.index(x)))
for i in range(n):
    if newlst[i][0]>=60:
        print(newlst[i][1])
        lst.remove(newlst[i])
for i in lst:
    print(i[1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107204725399](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241107204725399.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：



代码：

```python
n,m1,m2=[int(x) for x in input().split()]
lst1,lst2=[],[]
ans=[]
for _ in range(m1):
    row,col,item=[int(x) for x in input().split()]
    lst1.append([row,col,item])
for _ in range(m2):
    row,col,item=[int(x) for x in input().split()]
    lst2.append([row,col,item])
for i in lst1:
    for j in lst2:
        if i[1]==j[0]:
            ans.append([i[0],j[1],i[2]*j[2]])
ans.sort()
reans=[]
st1,st2=ans[0][0],ans[0][1]
for i in range(1,len(ans)):
    if ans[i][0]==st1 and ans[i][1]==st2:
        ans[i]=[st1,st2,ans[i][2]+ans[i-1][2]]
    else:
        reans.append(ans[i-1])
        st1,st2=ans[i][0],ans[i][1]
reans.append(ans[-1])
reans.sort()
for i in reans:
    print(*i)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241107212129792](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241107212129792.png)



### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：



代码：

```python
c=int(input())
for _ in range(c):
    n,m,b=[int(x) for x in input().split()]
    lst=[]
    for i in range(n):
        t,x=[int(x) for x in input().split()]
        lst.append([t,x])
    lst.sort(key=lambda x:(x[0],-x[1]))
    st=lst[0][0]
    b-=lst[0][1]
    stm=m
    m-=1
    if b<=0:
        print(st)
        continue
    for j in range(1,n):
        if lst[j][0]==st:
            if m>0:
                b-=lst[j][1]
                m-=1
        
        else:
            st=lst[j][0]
            m=stm
            m-=1
            b-=lst[j][1]
        if b<=0:
            print(st)
            break
    if b>0:
        print('alive')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107204821357](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241107204821357.png)



### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：



代码：

```python
n,m=[int(x) for x in input().split()]
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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107220014244](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241107220014244.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：我怎么就写了这么长的代码……



代码：

```python
s=input()
ans=0
res=s
d={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,'hundred':100,'thousand':1000,'million':1000000}
if 'negative' in res:
    res=res[9:]
a=''
record=[]
for i in res:
    if i!=' ':
        a+=i
    else:
        record.append(d[a])
        a=''
record.append(d[a])
reans1,reans2=0,0
if 1000000 in record:
    record2=record[:record.index(1000000)]
    if 1000 in record2:
        record3=record2[:record.index(1000)]
        if 100 in record3:
            reans2+=100*sum(record3[:record3.index(100)])
            record3=record3[record3.index(100)+1:]
        reans1+=1000*(sum(record3)+reans2)
        record2=record2[record2.index(1000)+1:]
    if 100 in record2:
        reans1+=100*sum(record2[:record2.index(100)])
        record2=record2[record2.index(100)+1:]
    reans1+=sum(record2)
    ans+=1000000*reans1
    
    record=record[record.index(1000000)+1:]
reans=0
if 1000 in record:
    record2=record[:record.index(1000)]
    if 100 in record2:
        reans+=100*sum(record2[:record2.index(100)])
        record2=record2[record2.index(100)+1:]
    ans+=1000*(sum(record2)+reans)
    record=record[record.index(1000)+1:]
if 100 in record:
    ans+=100*sum(record[:record.index(100)])
    record=record[record.index(100)+1:]
ans+=sum(record)
print([ans,-ans]['negative' in s])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107230759674](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241107230759674.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：



代码：

```python
n=int(input())
lst,end=[],[]
for _ in range(n):
    st,ed=[int(x) for x in input().split()]
    lst.append([st,ed])
    end.append(ed)
lst.sort(key=lambda x:(x[1],x[0]))
end.sort()
ans=1
rst,red=lst[0][0],lst[0][1]
for i in lst[1:]:
    if i[0]>red:
        ans+=1
        rst,red=i[0],i[1]
print(ans)
          
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108100614267](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241108100614267.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

呜呜呜呜呜废了废了

考试时鼠标不灵敏，第一题15分钟写完后复制时，一复制就乱码一复制就乱码，搞了快40分钟还没交上去，最后不得已换了台机子了呜呜呜

但这也不是我AC2的理由呜呜呜



