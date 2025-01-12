n=int(input())
lst,end=[],[]
for _ in range(n):
    st,ed=[int(x) for x in input().split()]
    lst.append([st,ed])
    end.append(ed)
lst.sort(key=lambda x:(x[1],x[0]))
end.sort()
ans=1
rst,red=lst[0][0],lst[0][1]
for i in lst[1:]:
    if i[0]>red:
        ans+=1
        rst,red=i[0],i[1]
print(ans)
            
        