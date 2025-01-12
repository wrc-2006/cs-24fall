'''
n=int(input())
v=[int(x) for x in input().split()]
u=sorted(v)
m=int(input())
for _ in range(m):
    type,l,r=[int(x) for x in input().split()]
    answer1=sum(v[l-1:r])
    answer2=sum(u[l-1:r])
    print([answer2,answer1][type==1])
'''    
###TLE

def prefix_sum(lst):
    prefix_sums=[0]*(len(lst)+1)
    for i in range(1,len(lst)+1):
        prefix_sums[i]=prefix_sums[i-1]+lst[i-1]
    return prefix_sums
n=int(input())
v=[int(x) for x in input().split()]
u=sorted(v)
m=int(input())
sum_v=prefix_sum(v)
sum_u=prefix_sum(u)
for _ in range(m):
    type,l,r=[int(x) for x in input().split()]
    answer1=sum_v[r]-sum_v[l-1] 
    answer2=sum_u[r]-sum_u[l-1]
    print([answer2,answer1][type==1])
