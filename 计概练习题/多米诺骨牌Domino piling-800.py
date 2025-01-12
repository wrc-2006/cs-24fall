M,N=map(int,input().split())
if (M*N)%2==0:
    print(M*N//2)
else:
    print((M*N-1)//2)