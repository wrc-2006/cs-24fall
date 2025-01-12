h=int(input())
courses=int(input())
lst_sc=[]
for _ in range(courses):
    s,c=map(float,input().split())
    lst_sc.append([s,c])
h*=2
h-=0.5*courses
lst_sc.sort(key=lambda x:x[0]*x[1],reverse=True)
ans=0
for s,c in lst_sc:
    if h>5/s:
        h-=5/s
        ans+=5*c
    else:
        ans+=c*h*s
        break
print(f'{ans:.1f}')
