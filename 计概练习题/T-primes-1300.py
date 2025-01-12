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
n=int(input())
x=[int(x) for x in input().split()]
lst=is_prime(1000000)
for i in x:
    sqrt_i=i**0.5
    if (sqrt_i)%1==0:
        if lst[int(sqrt_i)]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
        
###真的很不容易啊