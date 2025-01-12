'''
n,m=map(int,input().split())         
s=[int(x) for x in input().split()]
num=0
lst=[]
for i in s:
    if i<0:
        num+=1
        lst.append(i)
if num<=m:
    print(abs(sum(lst)))
else:
    lst=sorted(lst)
    print(abs(sum(lst[0:m])))
'''

n,m=map(int,input().split())
s=[int(x) for x in input().split()]
s.sort()
num=0
for i in range(m):
    if s[i]>0:
        break
    num+=s[i]
print(num)