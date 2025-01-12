# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by Hongfei Yan==（请改为同学的姓名、院系）==



**说明：**

1）Oct⽉考： AC6==（请改为同学的通过数）== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：



代码

```python

k=int(input())
s=input()
new_s=''
for i in s:
    if (65<=ord(i)<=90 and 65<=ord(i)-k<=90) or (97<=ord(i)<=122 and 97<=ord(i)-k<=122):
        new_s+=chr(ord(i)-k)
    elif 65<=ord(i)<=90:
        m=ord(i)-k
        while m<65:
            m+=26
        new_s+=chr(m)
    else:
         n=ord(i)-k
         while n<97:
             n+=26
         new_s+=chr(n)
print(new_s)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241012120342553](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241012120342553.png)



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：



代码

```python

a,b=[x for x in input().split()]
print(int(a[:2])+int(b[:2]))
```



代码运行截图 ==（至少包含有"Accepted"）==



![image-20241012120409562](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241012120409562.png)

### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：



代码

```python
n=int(input())
lst=[[0,'1'],[1,'0'],[2,'X'],[3,'9'],[4,'8'],[5,'7'],[6,'6'],[7,'5'],[8,'4'],[9,'3'],[10,'2']]
for _ in range(n):
    s=input()
    num=(7*int(s[0])+9*int(s[1])+10*int(s[2])+5*int(s[3])+8*int(s[4])+4*int(s[5])+2*int(s[6])+int(s[7])+6*int(s[8])+3*int(s[9])+7*int(s[10])+9*int(s[11])+10*int(s[12])+5*int(s[13])+8*int(s[14])+4*int(s[15])+2*int(s[16]))%11
    print(['NO','YES'][[num,s[-1]]in lst])

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==



![image-20241012120454849](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241012120454849.png)

### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：



代码

```python

n=int(input())
while True:
    if n==1:
        print('End')
        break
    elif n%2!=0:
        print(f'{n}*3+1={n*3+1}')
        n=n*3+1
    else:
        print(f'{n}/2={n//2}')
        n//=2
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241012120520443](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241012120520443.png)



### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：



##### 代码

```python
# 
s=input()
lst1=[0,1,2,3,4,5,6,7,8,9]
lst2=['','I','II','III','IV','V','VI','VII','VIII','IX']
if s[0] in [str(i) for i in range(0,10)]:
    t=int(s)
    new_s=''
    num_M=t//1000
    t%=1000
    new_s+='M'*num_M
    num_bai=t//100
    if num_bai in [4,9]:
        new_s+=['CD','CM'][num_bai==9]
    else:
        m=100*t//100
        if m>=500:
            new_s=new_s+'D'+'C'*((m-500)//100)
        else:
            new_s+='C'*(m//100)
    t%=100
    num_shi=t//10
    if num_shi in [4,9]:
        new_s+=['XL','XC'][num_shi==9]
    else:
        n=10*t//10
        if n>=50:
            new_s=new_s+'L'+'X'*((n-50)//10)
        else:
            new_s+='X'*(n//10)
    t%=10
    new_s+=lst2[lst1.index(t)]
    print(new_s)
else:
    newnum=0
    lst3=['I','V','X','L','C','D','M']
    lst4=[1,5,10,50,100,500,1000]
    newlst=[]
    for i in s:
        newlst.append(lst4[lst3.index(i)])
    for i in range(len(newlst)-1):
        if newlst[i]>=newlst[i+1]:
            newnum+=newlst[i]
        else:
            newnum=newnum-newlst[i]
    newnum+=lst4[lst3.index(s[-1])]
    print(newnum)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241012120628292](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241012120628292.png)



### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：还是不理解字典序，看答案貌似就是直接比大小？？可字典序的定义好像不是这个啊，不过也可能是因为我答案还没有搞懂，两天没做出来一道题哈哈哈哈



代码

```python
n,d=[int(x) for x in input().split()]
lst=[]
check=[False]*n
for _ in range(n):
    h=int(input())
    lst.append(h)
new_lst=[]
while False in check:
    buffer=[]
    i=0
    while i<len(lst):
        if check[i]:
            i+=1
            continue
        if buffer==[]:
            buffer.append(lst[i])
            check[i]=True
            maxh,minh=lst[i],lst[i]
            continue
        maxh=max(maxh,lst[i])
        minh=min(minh,lst[i])
        if maxh-lst[i]<=d and lst[i]-minh<=d:
            buffer.append(lst[i])
            check[i]=True
        i+=1
    buffer.sort()
    new_lst.extend(buffer)
print('\n'.join(map(str,new_lst)))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241012120806446](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241012120806446.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==



好难好累好烦，想在这里浅浅地发一个疯:

啊啊啊啊根本干不来啊，在B站大学上根本没学到什么东西啊，好累好难

没有起飞，感觉我掉下来了



![image-20241012121044243](C:\Users\lp\AppData\Roaming\Typora\typora-user-images\image-20241012121044243.png)



