t=int(input())
for i in range(t):
    s=[int(x) for x in input().split()]
    s.sort()
    if s[2]==s[0]+s[1]:
        print('YES')
    else:
        print('NO')