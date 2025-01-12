'''
n=int(input())
potion=[int(x) for x in input().split()]
health=0
positive=0
negative=[]
for i in potion:
    if i>=0:
        positive+=1
        health+=i
    else:
        negative.append(i)
        health+=i
        if health<0:
            health-=min(negative)
            negative.remove(min(negative))
print(positive+len(negative))
'''

#使用堆
import heapq
n=int(input())
potion=[int(x) for x in input().split()]
health=0
consume=[]
for i in potion:
    if i>=0:
        health+=i
        heapq.heappush(consume,i)
    else:
        heapq.heappush(consume,i)
        health+=i
        if health<0:
            health-=heapq.heappop(consume)
print(len(consume))

