t=int(input())
for _ in range(t):
    e,f=[int(x) for x in input().split()]
    coin=f-e
    n=int(input())
    price,weight=[],[]
    for __ in range(n):
        p,w=[int(x) for x in input().split()]
        price.append(p)
        weight.append(w)
    dp=[0]+[float('inf')]*10000
    for i in range(1,coin+1):
        for j in range(n):
            if weight[j]<=i:
                dp[i]=min(dp[i],dp[i-weight[j]]+price[j])
    if dp[coin]==float('inf'):
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {dp[coin]}.')