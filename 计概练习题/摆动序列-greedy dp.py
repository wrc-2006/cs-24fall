n=int(input())
lst=[int(x) for x in input().split()]
if n>=2:
    newlst=[lst[i]-lst[i-1] for i in range(1,n)]
else:
    newlst=[0]
for i in newlst:
    if i!=0:
        check=i
        break
else:
    check=0
ans=[1,2][check!=0]
for i in newlst:
    if i*check<0:
        ans+=1
        check=i
print(ans)
    