s=input()
lst=[]
a=0
for i in s:
    if i not in lst:
        lst.append(i)
if len(lst)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')