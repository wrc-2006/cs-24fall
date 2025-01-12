'''
while True:
    n,m=[int(x) for x in input().split()]
    if n==0 and m==0:
        break
    lst=[0]*n
    p=m
    i=0
    while True:
        if lst[i]==0:
            m-=1
        if m==0:
            lst[i]=1
            m=p
        i+=1
        if i==n:
            i=0
        if lst.count(0)==1:
            break
    print(lst.index(0)+1)
'''

###答案解法
def hot_potato(lst,num):   ###不知道给函数取啥名就照着答案取了，虽然不知道答案为什么取这个名字
    while len(lst)>1:
        for i in range(num-1):
            lst.append(lst.pop(0))
        lst.pop(0)
    return lst.pop(0)
while True:
    n,m=[int(x) for x in input().split()]
    if n==0 and m==0:
        break
    lst=[int(i) for i in range(1,n+1)]
    print(hot_potato(lst,m))
        