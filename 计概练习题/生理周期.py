n=0
while True:
    p,e,i,d=[int(x) for x in input().split()]
    if p<0:
        break
    n+=1
    for j in range(1,1000):
        if ((p+23*j)-e)%28==0 and ((p+23*j)-i)%33==0:
            day=p+23*j
            break
    print(f'Case {n}: the next triple peak occurs in {day-d} days.')