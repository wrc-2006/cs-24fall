s=list(input())
m='hello'
i=0
lst=[]
for _ in range(len(s)):
    if s[_]==m[i]:
        i+=1
        lst.append(s[_])
        if i>=5:
            break
if lst==list('hello'):
    print('YES')
else:
    print('NO')