n=int(input())
s=[x for x in input().split()]
maxn,minn='',''
s.sort(reverse=True)
while True:
    exchange=0
    for i in range(len(s)-1):
        if s[i+1] in s[i]:
            if s[i+1]+s[i]>s[i]+s[i+1]:
                s[i],s[i+1]=s[i+1],s[i]
                exchange+=1
    if exchange==0:
        break
        
for i in s:
    maxn+=i
s.reverse()
for i in s:
    minn+=i
print(int(maxn),int(minn))