'''
import math
t=int(input())
for _ in range(t):
    n=int(input())
    num_sum=0
    for i in range(1,n+1):
        if int(math.log2(i))==math.log2(i):
            num_sum-=i
        else:
            num_sum+=i
    print(num_sum)
'''
#好好好，又又又又又TLE了

t=int(input())      
for _ in range(t):
    n=int(input())
    num_sum=0
    sum1=(n+1)*n//2
    m=0
    for i in range(n):
        if 2**i>n:
            m=i
            break
    sum2=2**m-1
    num_sum=sum1-2*sum2 
    print(num_sum)