def permutation(s):
    ans=[]
    if len(s)==0:
        return [[]]
    for i in range(len(s)):
        current=s[i]
        remain=s[:i]+s[i+1:]
        repermutation=permutation(remain)
        for a in repermutation:
            ans.append([current]+a)
    return ans
    
n=int(input())
s=[int(x) for x in range(1,n+1)]
ans=permutation(s)
for i in ans:
    print(*i)
