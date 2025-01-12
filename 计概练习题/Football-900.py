s=input()
a=1 #相同数字的连续个数
b=s[0] #表示两队球员即1或0
lst=[]
for i in s[1:]:
    if b==i:
        a+=1
    else:
       b=i
       lst.append(a)
       a=1
    lst.append(a)
if max(lst)>=7:
    print('YES')
else:
    print('NO')
    