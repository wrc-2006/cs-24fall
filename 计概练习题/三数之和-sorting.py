s=sorted([int(x) for x in input().split()])
res=set()
for i in range(len(s)-2):
    if i >0 and s[i]==s[i-1]:
        continue
    d={}
    for x in s[i+1:]:
        if x not in d:
            d[-s[i]-x]=1
        else:
            res.add((s[i],-s[i]-x,x))
print(len(res))
