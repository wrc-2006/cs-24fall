n=int(input())
s=0
for i in range(n+1):
    if i%7!=0 and '7' not in str(i):
        s+=i**2
print(s)