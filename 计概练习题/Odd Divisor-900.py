'''
t=int(input())
for i in range(t):
    n=int(input())
    lst=[]
    for a in range(2,n+1):
        if n%a==0 and a%2!=0:
            print('YES')
            lst.append(a)
            break            
    if bool(lst)==False:
        print('NO')
'''

t=int(input())
for i in range(t):
    n=int(input())
    while n%2==0:
        n//=2
    if n>1:
        print('YES')
    else:
        print('NO')
        
         
