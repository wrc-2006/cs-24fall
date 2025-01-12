from math import sqrt
def mo(n):
    for i in range(1,int(sqrt(n))+1):
        if sqrt(n-i**2)%1==0 and n-i**2>0:
            return True
    return False

m=int(input())
x=[int(x) for x in input().split()]
for i in x:
    if mo(i):
        print(bin(i),oct(i),hex(i))