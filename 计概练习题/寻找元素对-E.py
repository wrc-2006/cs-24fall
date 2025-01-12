n=int(input())
s=sorted([int(x) for x in input().split()])
k=int(input())
num=0
for i in s:
    if k-i in s and i<k-i:
        num+=1
print(num)