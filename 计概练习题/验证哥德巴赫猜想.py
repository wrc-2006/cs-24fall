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
    
x=int(input())
lst=is_prime(2000)
ans=[]
if x<6 or x%2!=0:
    print('Error!')
else:
    for i in range(2,x):
        if x-i<i:
            break
        if lst[i] and lst[x-i]:
            ans.append((i,x-i))
    for i in ans:
        print(f'{x}={i[0]}+{i[1]}')