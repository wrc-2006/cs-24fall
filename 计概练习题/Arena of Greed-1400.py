'''
t=int(input())
for _ in range(t):
    n=int(input())
    ans=0
    while n>0:
        if n%2!=0:
            ans+=1
            n-=1
            n//=2
        else:
            ans+=n//2
            n//=2
            if n//2==0:
                n//=2
            else:
                n-=1
    print(ans)
    
果然没这么简单，TLE了……
'''
