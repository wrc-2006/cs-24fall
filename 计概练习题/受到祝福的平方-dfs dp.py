from math import sqrt
def is_sqrt(n):
    if int(sqrt(n))**2==n and n>0:
        return True
    else:
        return False
    
def dfs(a):
    global ans
    if a=='':
        ans='Yes'
        return
    for i in range(1,len(a)+1):
        if is_sqrt(int(a[:i])):
            dfs(a[i:])
    
a=input()  
ans='No'
dfs(a)
print(ans)
