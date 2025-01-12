n=int(input())
lst=[]
for i in range(2,n):
    while n%i==0:
        n//=i
        lst.append(i)
if n>1:
    lst.append(n)
if len(set(lst))<len(lst):
    print(0)
elif len(lst)%2==0:
    print(1)
else:
    print(-1)

