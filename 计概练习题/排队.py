n,d=[int(x) for x in input().split()]
lst=[]
check=[False]*n
for _ in range(n):
    h=int(input())
    lst.append(h)
new_lst=[]
while False in check:
    buffer=[]
    i=0
    while i<len(lst):
        if check[i]:
            i+=1
            continue
        if buffer==[]:
            buffer.append(lst[i])
            check[i]=True
            maxh,minh=lst[i],lst[i]
            continue
        maxh=max(maxh,lst[i])
        minh=min(minh,lst[i])
        if maxh-lst[i]<=d and lst[i]-minh<=d:
            buffer.append(lst[i])
            check[i]=True
        i+=1
        buffer.sort()
        new_lst.extend(buffer)
print('\n'.join(map(str,new_lst)))
        
            