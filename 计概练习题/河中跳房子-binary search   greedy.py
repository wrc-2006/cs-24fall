'''
l,n,m=[int(x) for x in input().split()]
stone=[0]
for _ in range(n):
    stone.append(int(input()))
stone.append(l)
distance=[stone[i]-stone[i-1] for i in range(1,n+2)]
while m>0:
    position=distance.index(min(distance))
    if position==0:
        stone.pop(1)
        distance[1]+=distance[0]
    elif position==len(distance)-1:
        stone.pop(-2)
        distance[-2]+=distance[-1]
    else:
        if distance[position-1]>=distance[position+1]:
            stone.pop(position+1)
            distance[position+1]+=distance[position]
        else:
            stone.pop(position)
            distance[position-1]+=distance[position]
    distance.pop(position)
    m-=1
print(min(distance))
'''
##binary search
l,n,m=[int(x) for x in input().split()]
stone=[0]
for _ in range(n):
    stone.append(int(input()))
stone.append(l)
def check(x):
    num=0
    now=0
    for i in range(1,n+2):
        if stone[i]-now<x:
            num+=1
        else:
            now=stone[i]
    if num>m:
        return True
    else:
        return False
lo,hi=0,l+1
ans=0
while lo<hi:
    mid=(lo+hi)//2
    if check(mid):
        hi=mid
    else:
        lo=mid+1
        ans=mid
print(ans)
    