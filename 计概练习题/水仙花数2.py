a,b=map(int,input().split())
lst=[]
for i in range(a,b+1):
    bai_wei=i//100
    shi_wei=(i-i//100*100)//10
    ge_wei=i-bai_wei*100-shi_wei*10
    if bai_wei**3+shi_wei**3+ge_wei**3==i:
        lst.append(i)
if lst==[]:
    print('NO')
else:
    print(*lst)

