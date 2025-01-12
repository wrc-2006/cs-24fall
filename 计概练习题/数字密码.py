s=int(input())
m=6
while True:
    if s%m==0:
        print(s//m)
        break
    else:
        m+=1