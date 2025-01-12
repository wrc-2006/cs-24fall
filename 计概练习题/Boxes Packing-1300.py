from collections import Counter
n=int(input())
s=sorted([int(x) for x in input().split()])
new_s=dict(Counter(s))
ans=0
lst=[]
for key,item in new_s.items():
    lst.append(item)
box=lst[0]
for i in range(1,len(lst)):
    if box<=lst[i]:
        box=lst[i]
print(box)
