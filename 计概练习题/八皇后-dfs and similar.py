def permutation(lst):
    ans=[]
    if len(lst)==0:
        return [[]]
    for i in range(len(lst)):
        current=lst[i]
        remain=lst[:i]+lst[i+1:]
        permutations=permutation(remain)
        for a in permutations:
            ans.append([current]+a)
    return ans
n=int(input())
lst=[1,2,3,4,5,6,7,8]
ans=permutation(lst)
newans=[]
for item in ans:
    for i in range(len(item)):
        for j in range(i+1,len(item)):
            if j-i==abs(item[i]-item[j]):
                break
        else:
            continue
        break
    else:
        newans.append(item)
newans.sort()
for _ in range(n):
    b=int(input())
    print(''.join(map(str,newans[b-1])))    
