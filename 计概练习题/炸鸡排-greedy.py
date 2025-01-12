n,k=[int(x) for x in input().split()]
t=[int(x) for x in input().split()]
t.sort(reverse=True)
maxt=sum(t)/k
cnt=1
for i in range(len(t)):
    if t[i]>maxt:
        maxt=sum(t[i+1:])/(k-cnt)
        cnt+=1
print(f'{maxt:.3f}')
