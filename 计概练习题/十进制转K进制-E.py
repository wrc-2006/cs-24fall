n,k=[int(x) for x in input().split()]
ans=''
lst=[10,11,12,13,14,15]
while True:
    if n%k<10:
        ans+=f'{n%k}'
    else:
        ans+=['A','B','C','D','E','F'][lst.index(n%k)]
    if n//k<k:
        ans+=f'{n//k}'
        break
    n//=k
reversed_ans=ans[::-1]
print(reversed_ans)