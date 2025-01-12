a=int(input())
if a%2!=0:
    print('0 0')
elif a%4==0:
    m=a//4
    n=a//2
    print(m,n)
else:
    m=a//4+1
    n=a//2
    print(m,n)

