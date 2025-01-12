s=input().lower()
new_s=''
for i in s:
    if i not in ['a','o','y','e','u','i']:
        new_s+='.'+i
print(new_s)