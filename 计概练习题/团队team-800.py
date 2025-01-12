n=int(input())
s=0
for i in range(n):
    a,b,c=map(int,input().split())
    if a+b+c==2 or a+b+c==3:
        s+=1
print(s)