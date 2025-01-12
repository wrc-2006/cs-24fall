n,max_w=map(int,input().split())
lst=[]
for _ in range(n):
    v,w=map(int,input().split())
    lst.append([v/w,w]) 
new_lst=sorted(lst,reverse=True)
cost=0
for s in new_lst:
    if max_w<=s[1]:
        cost+=max_w*s[0]
        break
    else:
        cost+=s[1]*s[0]
        max_w-=s[1]
print('%.1f' %(cost))