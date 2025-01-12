n,a,b=[int(x) for x in input().split()]
ra,rb=a,b
water=[int(x) for x in input().split()]
cnt=0
left,right=0,n-1
while left<right:
    if water[left]>a:
        a=ra
        cnt+=1
    a-=water[left]
    left+=1
    if water[right]>b:
        b=rb
        cnt+=1
    b-=water[right]
    right-=1
if right==left:
    if water[left]>max(a,b):
        cnt+=1
print(cnt)



