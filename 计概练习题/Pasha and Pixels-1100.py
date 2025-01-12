'''
n,m,k=[int(x) for x in input().split()]
lst=[]
for _ in range(k):
    i,j=[int(x) for x in input().split()]
    if [i,j] not in lst:
        lst.append([i,j])
        if [i,j-1] in lst:
            if ([i+1,j] in lst and [i+1,j-1] in lst) or ([i-1,j] in lst and [i-1,j-1] in lst):
                print(_+1)
                break
        elif [i,j+1] in lst:
            if ([i+1,j] in lst and [i+1,j+1] in lst) or ([i-1,j] in lst and [i-1,j+1] in lst):
                print(_+1)
                break
else:
    print(0)
    
in判断耗时太多
'''
n,m,k=[int(x) for x in input().split()]
lst=[]
for _ in range(n+2):
    lst.append([False]*(m+2))   #n+2,m+2避免索引超出范围
for _ in range(k):
    i,j=[int(x) for x in input().split()]
    lst[i][j]=True
    if lst[i][j-1]:
        if (lst[i+1][j] and lst[i+1][j-1]) or (lst[i-1][j] and lst[i-1][j-1]):
            print(_+1)
            break
    elif lst[i][j+1]:
        if (lst[i+1][j] and lst[i+1][j+1]) or (lst[i-1][j] and lst[i-1][j+1]):
            print(_+1)
            break
else:
    print(0)