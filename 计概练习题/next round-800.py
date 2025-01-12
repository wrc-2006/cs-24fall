n,k=[int(x) for x in input().split()] 
p=list(map(int,input().split()))
s=0
for item in p:
    if item>=p[k-1] and item>0:
        s+=1
print(s)
