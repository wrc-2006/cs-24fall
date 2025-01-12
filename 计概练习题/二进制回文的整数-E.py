n=int(input())
num=list('{0:b}'.format(n))
if list(reversed(num))==num:
    print('Yes')
else:
    print('No')