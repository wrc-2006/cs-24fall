n,m1,m2=[int(x) for x in input().split()]
lst1,lst2=[],[]
ans=[]
for _ in range(m1):
    row,col,item=[int(x) for x in input().split()]
    lst1.append([row,col,item])
for _ in range(m2):
    row,col,item=[int(x) for x in input().split()]
    lst2.append([row,col,item])
for i in lst1:
    for j in lst2:
        if i[1]==j[0]:
            ans.append([i[0],j[1],i[2]*j[2]])
ans.sort()
reans=[]
st1,st2=ans[0][0],ans[0][1]
for i in range(1,len(ans)):
    if ans[i][0]==st1 and ans[i][1]==st2:
        ans[i]=[st1,st2,ans[i][2]+ans[i-1][2]]
    else:
        reans.append(ans[i-1])
        st1,st2=ans[i][0],ans[i][1]
reans.append(ans[-1])
reans.sort()
for i in reans:
    print(*i)