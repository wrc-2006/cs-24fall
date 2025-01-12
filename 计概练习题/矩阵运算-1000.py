a,b,c=[],[],[]

row_1,col_1=[int(x) for x in input().split()]
for _ in range(row_1):
    a.append([int(x) for x in input().split()])
row_2,col_2=[int(x) for x in input().split()]
for _ in range(row_2):
    b.append([int(x) for x in input().split()])
row_3,col_3=[int(x) for x in input().split()]
for _ in range(row_3):
    c.append([int(x) for x in input().split()])
    
if col_1==row_2 and row_1==row_3 and col_2==col_3:
    for m in range(row_3):
        new_row=[]
        for n in range(col_3):
            s=0
            for p in range(col_1):
                s+=a[m][p]*b[p][n]
            s+=c[m][n]
            new_row.append(s)
        print(*new_row)
else:
    print('Error!')            