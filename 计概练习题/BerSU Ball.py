n=int(input())
a=sorted([int(x) for x in input().split()])
m=int(input())
b=sorted([int(x) for x in input().split()])
num=0
for i in a:
    for j in b:
        if abs(i-j)<=1:
            num+=1
            b.remove(j)
            break
print(num)