n=int(input())
s=[int(x) for x in input().split()]
sum=0
officer=0
for i in s:
    if i>0:
        officer+=i
    elif i <0 and officer==0:
        sum+=1
    else:
        officer-=1 
print(sum)
         
