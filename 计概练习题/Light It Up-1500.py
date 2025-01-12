'''
def change(lst):
    time1,time2=0,0
    for i in range(n+1):
        if i%2==0:
            time1+=lst[i]
            arr[i]=time1
        else:
            time2+=lst[i]
            arr[i]=time2
    return arr,time2
#将lst偶数索引和奇数索引存入arr中，同时由于不知道n奇偶，取出time2作为总奇数索引之和
n,m=[int(x) for x in input().split()]
arr=[0]*(n+1)
a=[int(x) for x in input().split()]
a.append(m)
lst=[a[i]-a[i-1] for i in range(1,n+1)] 
lst.insert(0,a[0]) #将每段时间差加入列表中，若不改变，灯亮时间即为偶数索引之和
ans=[]
ans0=0
for i in range(n+1):
    if i%2==0:
        ans0+=lst[i]  #没有改变任何程序
ans.append(ans0)
arr,time2=change(lst)
for i in range(3,n+1,2):
    elans=arr[i-1]+time2-arr[i-2]-1 #若在第i个后加个改变程序，之后的奇数索引减一加上之前的偶数索引之和即为灯亮时间
    ans.append(elans)
ans.append(arr[0]+time2-1) #将i为1单独拿出来算，避免索引超出范围
print(max(ans))
'''
'''
终于自己写出来了，虽然思路十分凌乱，代码写的也非常不美观，希望之后看代码时还能理解我现在的想法
感觉能想出这种野路子的我也是个天才

好吧，答案思路差不多，但相比之下，我的代码……
'''

n, m = map(int, input().split())
a = [0] + [int(x) for x in input().split()] + [m]
tot = ans = s = 0
for i in range(1, len(a), 2):
    tot += a[i] - a[i-1]
ans = tot						  	#总开灯时间
for i in range(2, len(a), 2):
    s += a[i-1] - a[i-2]			#前 i 次开灯时间
    if a[i] > a[i-1] + 1:			#若关灯时长大于 1
        t = tot -s					#导出后 n-i 次开灯时间
        ans = max(ans, s + m-a[i-1]-t - 1)	#之前奇数项+之后偶数项-1
print(ans)