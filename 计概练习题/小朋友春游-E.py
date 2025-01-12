n=int(input())
s=[int(x) for x in input().split()]
mine,others,lst=[],[],[]
for i in s:
    if i>n:
        others.append(i)
    else:
        mine.append(i)
for i in range(1,n+1):
    if i not in mine:
        lst.append(i)
print(*sorted(lst))
print(*sorted(others))
        