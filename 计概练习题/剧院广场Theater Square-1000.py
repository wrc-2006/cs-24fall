'''
n,m,a=map(int,input().split())
if m%a!=0 and n%a!=0:
    print((m//a+1)*(n//a+1))
elif m%a==0 and n%a!=0:
    print(m//a*(n//a+1))
elif m%a!=0 and n%a==0:
    print(n//a*(m//a+1))
else:
    print(m//a*n//a)
'''

import math
m,n,a=[int(x) for x in input().split()]
print(math.ceil(m/a)*math.ceil(n/a))