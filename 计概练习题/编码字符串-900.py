s=input().lower()
num=s[0]
key=1
for i in s[1:]:
    if i==num:
        key+=1
    else:
        print('('+num+','+str(key)+')',end='')
        num=i
        key=1
print('('+num+','+str(key)+')')