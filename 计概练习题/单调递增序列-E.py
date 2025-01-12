n=int(input())
s=[int(x) for x in input().split()]
for i in range(1,len(s)):
    if s[i]<s[i-1]:
        print('NO')
        break
else:
    print('YES')