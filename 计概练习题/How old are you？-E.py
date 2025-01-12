x=int(input())
while True:
    if x%2==0:
        print(f'{x}/2={x//2}')
        x//=2
        if x==1:
            break
    else:
        print(f'{x}*3+1={x*3+1}')
        x=x*3+1
    