n=int(input())
s=[int(x) for x in input().split()]
s.sort(reverse=True)
all_sum=sum(s)
mine=0
num=0
for i in s:
    mine+=i
    num+=1
    if mine>all_sum-mine:
        print(num)
        break
        
    