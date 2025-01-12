n=int(input())
service_time=[int(x) for x in input().split()]
service_time.sort()
waiting_time=0
num=0
for i in service_time:
    if waiting_time<=i:
        num+=1
        waiting_time+=i
print(num)