n=int(input())
for _ in range(n):
    s=input()
    year=int(s[0:4])
    d=int(s[6:])
    m=int(s[4:6])
    if m<3:
        m+=12
        c=int(str(year-1)[0:2])
        y=int(str(year-1)[2:4])
    else:
        c=int(str(year)[0:2])
        y=int(str(year)[2:4])
    w=(y+y//4+c//4-2*c+26*(m+1)//10+d-1)%7
    dic={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    print(dic[w])
        