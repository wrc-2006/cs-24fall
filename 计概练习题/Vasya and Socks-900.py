n,m=[int(x) for x in input().split()]
num_socks=n
day=0
while True:
    day+=1
    num_socks-=1
    if day%m==0:
        num_socks+=1
    if num_socks==0:
        break
print(day)