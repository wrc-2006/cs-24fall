import sys
from functools import lru_cache
sys.setrecursionlimit(1<<30)
@lru_cache(maxsize=None)

def step(n):
    if dp[n]!=0:
        return dp[n]
    else:
        dp[n]=step(n-1)+step(n-2)
        return dp[n]

n=int(input())
dp=[0]*5001
dp[1],dp[2]=1,2
print(step(n))