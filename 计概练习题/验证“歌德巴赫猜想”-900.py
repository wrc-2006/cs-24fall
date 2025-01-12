def is_prime(n):
    if n==3:
        return True
    elif n>3 and n%2!=0:
        m=1
        for i in range(3,n,2):
            if n%i==0:
                m=0
                break
        if m==0:
            return False
        else:
            return True
    else:
        return False
x=int(input())
if x<6 or x%2!=0:
    print('Error!')
else:
    for y in range(3,x//2+1):
        if is_prime(y) and is_prime(x-y):
            print(f'{x}={y}+{x-y}')