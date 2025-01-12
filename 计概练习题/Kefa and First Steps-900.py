n=int(input())
s=[int(x) for x in input().split()]
lst=[]
m=s[0]
num=1
for i in s[1:]:
    if i>=m:
        num+=1
        m=i
    else:
        m=i
        lst.append(num)
        num=1
lst.append(num)
print(max(lst))