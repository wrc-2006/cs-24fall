def primes(n):
    lst=[True]*(n+1)
    lst[1]=False
    primes=[]
    for i in range(2,n+1):
        if lst[i]:
            primes.append(i)
        for p in primes:
            if i*p>n:
                break
            lst[i*p]=False
            if i%p==0:
                break
    return primes
s=int(input())
ans=[]
for i in primes(s):
    if s-i in primes(s):
        ans.append(i*(s-i))
print(max(ans))

###将所有质数都列举出来再找太耗时了