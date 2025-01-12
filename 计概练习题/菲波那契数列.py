'''
n=int(input())
lst=[1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765]
for _ in range(n):
    a=int(input())
    print(lst[a-1])
'''
###硬干！

'''
n=int(input())
for _ in range(n):
    lst=[1,1]
    a=int(input())
    if a<=2:
        print(1)
    else:
        while a>2:
            lst.append(lst[-1]+lst[-2])
            a-=1
        print(lst[-1])
太麻烦了
'''
from recviz import recviz
@recviz
def f(n):
    if n<=2:
        return 1
    if dp[n]!=0:
        return dp[n]
    else:
        dp[n]=f(n-1)+f(n-2)
        return dp[n]
dp=[0]*21
n=int(input())
for _ in range(n):
    a=int(input())
    print(f(a))
        