n=int(input())
num=0
num+=n//100
a=n%100
num+=a//20
b=a%20
num+=b//10
c=b%10
num+=c//5
d=c%5
num+=d
print(num)