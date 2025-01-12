n=int(input())
lst=[]
for _ in range(n):
    s=input()
    lst.append(s)
string=lst[0]
for i in lst[1:]:
    for j in range(min(len(string),len(i))):
        if string[j]!=i[j]:
            string=string[:j]
            break
    else:
        string=string[:min(len(string),len(i))]
print(string)
