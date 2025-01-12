from math import sqrt
def is_prime(n):
    lst=[True]*(n+1)
    primes=[]
    lst[1]=False
    for i in range(2,n+1):
        if lst[i]:
            primes.append(i)
        for p in primes:
            if i*p>n:
                break
            lst[i*p]=False
            if i%p==0:
                break
    return lst
    
m,n=[int(x) for x in input().split()]
lst=is_prime(10005)
for _ in range(m):
    grade=[int(x) for x in input().split()]
    ans=0
    for i in grade:
        if sqrt(i)%1==0:
            if lst[int(sqrt(i))]:
                ans+=i
    res=ans/len(grade)
    print(0 if res==0 else f'{res:.2f}')
