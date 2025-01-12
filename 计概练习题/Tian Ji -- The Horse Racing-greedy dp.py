while True:
    n=int(input())
    if n==0:
        break
    ans=0
    tian=sorted([int(x) for x in input().split()],reverse=True)
    king=sorted([int(x) for x in input().split()],reverse=True)
    while tian:
        if tian[0]>king[0]:
            ans+=1
            del tian[0]
            del king[0]
        else:
            if tian[-1]>king[-1]:
                ans+=1
                del tian[-1]
                del king[-1]
            elif tian[-1]<king[0]:
                ans-=1
                del tian[-1]
                del king[0]
            else:
                del tian[-1]
                del king[0]
                
    print(200*ans)