n=int(input())
t=[int(x) for x in input().split()]
lst=[]
for i,time in enumerate(t,1):
    lst.append([time,i])
lst.sort()
for i in lst:
    print(i[1],end=' ')
print()
waiting=0
m=1
for i in lst[:-1]:
    waiting+=i[0]*(n-m)
    m+=1
print(f'{waiting/n:.2f}')