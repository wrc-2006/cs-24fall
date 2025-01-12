'''
组合1
def combination(s,k):
    if k==0:
        return [[]]
    else:
        arr=[]
        for i in range(len(s)-k+1):
            a=s[i]
            remain=s[i+1:]
            combinations=combination(remain,k-1)
            for j in combinations:
                arr.append([a]+j)
    return arr

n,k=[int(x) for x in input().split()]
s=[int(i) for i in range(1,n+1)]
arr=combination(s,k)
for i in arr:
    print(*i)
'''

'''
组合2
def combination(s,k):
    if k==0:
        return [[]]
    else:
        arr=[]
        for i in range(len(s)-k+1):
            a=s[i]
            remain=s[i+1:]
            combinations=combination(remain,k-1)
            for j in combinations:
                arr.append([a]+j)
    return arr
n,k=[int(x) for x in input().split()]
s=[int(x) for x in input().split()]
arr=combination(s,k)
for i in arr:
    print(*i)
'''

def combination(s,k):
    if k==0:
        return [[]]
    else:
        arr=[]
        for i in range(len(s)-k+1):
            a=s[i]
            remain=s[i+1:]
            combinations=combination(remain,k-1)
            for j in combinations:
                if [a]+j not in arr:
                    arr.append([a]+j)
    return arr
n,k=[int(x) for x in input().split()]
s=[int(x) for x in input().split()]
arr=combination(s,k)
for i in arr:
    print(*i)