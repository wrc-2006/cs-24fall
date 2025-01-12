n=int(input())
lst=[]
for b in range(2,n):
    for c in range(b,n):
        for d in range(c,n):
            m=b**3+c**3+d**3
            if m<=n**3 and (round(m**(1/3)))**3==m:
                a=round(m**(1/3)) 
                lst.append([a,b,c,d])
lst.sort()
for i in lst:
    print(f'Cube = {i[0]}, Triple = ({i[1]},{i[2]},{i[3]})')
    