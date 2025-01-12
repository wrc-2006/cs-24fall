n=int(input())
ans=[]
for x in range(n+1):
    for y in range(n+1):
        for z in range(n+1):
            if (x+y)%2==0 and (y+z)%3==0 and (x+y+z)%5==0:
                ans.append(x+y+z)
print(max(ans))
