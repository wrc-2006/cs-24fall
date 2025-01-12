def tower(n,A,B,C):
    if n==1:
        print(f'{A}->{C}')
    else:
        tower(n-1,A,C,B)
        print(f'{A}->{C}')
        tower(n-1,B,A,C)
n=int(input())
print(2**n-1)
A,B,C='A','B','C'
tower(n,A,B,C)