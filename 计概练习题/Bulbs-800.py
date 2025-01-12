'''
n,m=map(int,input().split())
lst=[]
for i in range(n):
    s=[int(x) for x in input().split()]
    del s[0]
    lst+=s
if set(lst)==set(range(1,m+1)):
    print('YES')
else:
    print('NO')
'''

n,m=map(int,input().split())
s=set()
for i in range(n):
    s.update(input().split()[1:])
'''
if len(s)==m:
    print('YES')
else:
    print('NO')
'''
print(['NO','YES'][len(s)==m])