n=int(input())
for _ in range(n):
    s=int(input())
    a=int(input())
    lst_a=[int(x) for x in input().split()]
    b=int(input())
    lst_b=[int(x) for x in input().split()]
    num=0
    for i in lst_a:
        if s-i in lst_b:
            num+=lst_b.count(s-i)
    print(num)