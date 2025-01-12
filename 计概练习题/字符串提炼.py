import math
s='.'
s+=input()
m=int(math.log2(len(s)))
ans=''
left=0
right=m
while left<=right:
    if left==right:
        ans+=s[2**left]
        break
    ans+=s[2**left]
    ans+=s[2**right]
    left+=1
    right-=1
print(ans)
