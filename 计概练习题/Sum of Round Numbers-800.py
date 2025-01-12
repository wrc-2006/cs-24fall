t=int(input())
for i in range(t):
    n=int(input())
    lst=[10000,1000,100,10,1 ]
    lst2=[]
    sum=0
    for item in lst:
        if n//item!=0:
            sum+=1
            lst2.append(n//item*item)
            n-=n//item*item
    print(sum)
    print(*lst2)
'''
    for _ in lst2:
        print(_,end=' ')
'''       
        
