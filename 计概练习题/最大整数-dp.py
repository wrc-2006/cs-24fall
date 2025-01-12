def check(x):
    if x=='':
        return 0
    else:
         return int(x)
    
m=int(input())
n=int(input())
s=[str(x) for x in input().split()]
s.sort(reverse=True)
while True:
    exchange=0
    for i in range(len(s)-1):
        if s[i+1] in s[i]:
            if s[i+1]+s[i]>s[i]+s[i+1]:
                s[i+1],s[i]=s[i],s[i+1]
                exchange+=1
    if exchange==0:
        break
dp=[['']*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if len(s[i-1])>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=str(max(check(dp[i-1][j]),int(dp[i-1][j-len(s[i-1])]+s[i-1])))
print(dp[n][m])