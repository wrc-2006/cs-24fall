s=input()
ans=0
length=1
num=int(s[0])
for i in s[1:]:
    if int(i)==num^1:
        length+=1
        num^=1
    else:
        num=int(i)
        ans=max(length,ans)
        length=1
ans=max(length,ans)
print(ans)