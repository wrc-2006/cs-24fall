t=int(input())
for _ in range(t):
    n=int(input())
    if n==1:
        print(0)
    else:
        p=q=0
        while n%3==0:
            p+=1
            n//=3
        while n%2==0:
            q+=1
            n//=2
        if n!=1 or p<q:
            print(-1)
        else:
            print(2*p-q)