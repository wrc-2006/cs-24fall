'''
s=input()
m=int(input())
answer=[]
for _ in range(m):
    num=0
    l,i=[int(x) for x in input().split()]
    for n in range(l,i):
        if s[n-1]==s[n]:
            num+=1
    answer.append(str(num))
print('\n'.join(answer))
'''

s=input()
m=int(input())
lst=[0]
num=0
for _ in range(1,len(s)):
    if s[_]==s[_-1]:
        num+=1
    lst.append(num)
for _ in range(m):
    l,i=[int(x) for x in input().split()]
    print(lst[i-1]-lst[l-1])