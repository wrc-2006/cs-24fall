'''
二分查找bisect
'''
import bisect
n=int(input())
x=sorted([int(x) for x in input().split()])
q=int(input())
lst_m=[]
for _ in range(q):
    ans=0
    m=int(input())
    print(bisect.bisect_right(x,m))
    
    