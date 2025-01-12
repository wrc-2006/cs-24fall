n=int(input())
num=0
for _ in range(n):
    s=input()
    num+=(s.count('###')-s.count('### ###')*2)//2
print(num)