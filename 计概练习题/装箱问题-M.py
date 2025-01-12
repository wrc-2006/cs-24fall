import math
lst=[0,5,3,1]
while True:
    s=[int(x) for x in input().split()]
    if s==[0,0,0,0,0,0]:
        break
    num=s[5]+s[4]+s[3]+math.ceil(s[2]/4)
    rest=s[3]*5+lst[s[2]%4]
    num+=max(0,math.ceil((s[1]-rest)/9))
    rest2=(num-s[5])*36-s[4]*25-s[3]*16-s[2]*9-s[1]*4
    num+=max(0,math.ceil((s[0]-rest2)/36))
    print(num)
