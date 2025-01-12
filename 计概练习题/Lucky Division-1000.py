n=int(input())
num=0
for i in [4,7,47,74,447,474,477,444,744,747,774,777]:
    if n%i==0:
        print('YES')
        break
    else:
        num+=1
if num==12:
    print('NO')
        