def pell(n,dp):
    if n==0:
        dp[0]=0
        return 0
    if n==1:
        dp[1]=1
        return 1
    if n==2:
        dp[2]=2
        return 2
    if dp[n]!=-1:
        return dp[n]
    else:
        dp[n]=(pell(n-1,dp)*2+pell(n-2,dp))%32767
        return dp[n]
dp=[-1]*150
dp[0],dp[1],dp[2]=0,1,2
n=int(input())
for _ in range(n):
    k=int(input())
    print(pell(k%150,dp))