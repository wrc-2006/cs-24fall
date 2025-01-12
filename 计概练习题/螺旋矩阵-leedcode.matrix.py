lst=eval(input())
arr=[]
row=len(lst)+2
col=len(lst[0])+2
lst=[[1000]*col]+[[1000]+i+[1000] for i in lst]+[[1000]*col]
i,j=1,1
direction=[[0,1],[1,0],[0,-1],[-1,0]]
index=0
dire=direction[0]
m,n=dire
lenth=(row-2)*(col-2)
while len(arr)<lenth:
    if lst[i][j]<1000:
        arr.append(lst[i][j])
        lst[i][j]=1000
        i+=m
        j+=n
    else:
        index=(index+1)%4
        dire=direction[index]
        i-=m
        j-=n
        m,n=dire
        i+=m
        j+=n
print(arr)
    
