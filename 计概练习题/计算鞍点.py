lst=[]
for _ in range(5):
    lst.append([int(x) for x in input().split()])
ans=[]
wmax,wmin=[],[]
for i in range(5):
    wmax.append([i,lst[i].index(max(lst[i]))])
    minh=lst[0][i]
    rj=0
    for j in range(1,5):
        if lst[j][i]<minh:
            minh=lst[j][i]
            rj=j
    wmin.append([rj,i])
for i in wmax:
    if i in wmin:
        ans.append(lst[i[0]][i[1]])
        hang,lie=i[0],i[1]
if ans==[]:
    print('not found')
else:
    print(hang+1,lie+1,*ans)