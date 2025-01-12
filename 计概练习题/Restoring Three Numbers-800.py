s=[int(x) for x in input().split()]
maximum=max(s)
s.remove(maximum)
for i in s:
    print(maximum-i,end=' ')