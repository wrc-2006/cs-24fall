n=int(input())
l_x=[]
l_y=[]
l_z=[]
for _ in range(n):
    x,y,z=map(int,input().split())
    l_x.append(x)
    l_y.append(y)
    l_z.append(z)
if sum(l_x)==0 and sum(l_y)==0 and sum(l_z)==0:
    print('YES')
else:
    print('NO')
    
    