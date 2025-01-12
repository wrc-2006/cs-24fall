n,l=[int(x) for x in input().split()]
a=set([int(x) for x in input().split()])
lst1=[]
for index,item in enumerate(a):
    lst1.append(item)
lst1.sort()
m=lst1[0]
lst2=[lst1[0]]
for i in range(1,len(lst1)):
    lst2.append(lst1[i]-m)
    m=lst1[i]
print(max(max(lst2)/2,min(lst1),l-max(lst1)))