for i in range(5):
    s=[int(x) for x in input().split()]
    if 1 in s:
        row=i
        a=s.index(1)
print(abs(2-a)+abs(2-row))

