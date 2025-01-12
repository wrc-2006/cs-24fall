'''
def prefix_sum(lst):
    prefix_sums=[0]*n
    prefix_sums[0]=lst[0][1]
    for i in range(1,n):
        prefix_sums[i]=prefix_sums[i-1]+lst[i][1]
    return prefix_sums
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    lst=list(zip(a,b))
    lst.sort()
    a.sort()
    ans=[]
    prefix_sums=prefix_sum(lst)
    for i in range(n):
        ans.append(max(a[i],prefix_sums[n-1]-prefix_sums[i]))
    ans.append(prefix_sums[n-1])
    ans.append(a[n-1])
    print(min(ans))    
'''
#答案思路相似，但实现更简单
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    lst=list(zip(a,b))
    ans=0
    lst.sort(reverse=True)
    for i in lst:
        ans+=i[1]
        if ans>=i[0]:
            ans=max(i[0],ans-i[1])
            break
    print(ans)