'''
def love(lst):
    if len(lst)<=1:
        return 'NO'
    else:
        right=lst[0][1]
        for i in lst[1:]:
            if i[0]>right:
                return 'YES'
            else:
                if i[1]<right:
                    right=i[1]
    return 'NO'

q=int(input())
lst=[]
for _ in range(q):
    a,l,r=input().split()
    l,r=int(l),int(r)
    if a=='+':
        lst.append((l,r))
        lst.sort()
        print(love(lst))
    else:
        lst.remove((l,r))
        print(love(lst))
TLE
'''
