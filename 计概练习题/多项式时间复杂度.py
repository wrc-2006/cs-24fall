s=input()
record=[]
num=['0','1','2','3','4','5','6','7','8','9']
string=''
nums=[]
for i in range(len(s)):
    if s[i] not in num:
        if string!='':
            nums.append(int(string))
        string=''
        if s[i]=='n':
            if i-1<0 or s[i-1]=='+':
                nums.append(1)
    else:
        string+=s[i]
nums.append(int(string))
for i in range(1,len(nums),2):
    if nums[i-1]!=0:
        record.append(nums[i])
if record==[]:
    print('n^0')
else:
    print(f'n^{max(record)}')