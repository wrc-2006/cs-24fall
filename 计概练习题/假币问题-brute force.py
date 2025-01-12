n=int(input())
for _ in range(n):
    coin={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0}
    check={'A':False,'B':False,'C':False,'D':False,'E':False,'F':False,'G':False,'H':False,'I':False,'J':False,'K':False,'L':False}
    for __ in range(3):
        a,b,c=[x for x in input().split()]
        if c=='even':
            for i in a+b:
                check[i]=True
                coin[i]=0
        if c=='up':
            for i in a:
                if not check[i]:
                    coin[i]+=1
            for j in b:
                if not check[j]:
                    coin[j]-=1
        if c=='down':
            for i in a:
                if not check[i]:
                    coin[i]-=1
            for j in b:
                if not check[j]:
                    coin[j]+=1
    ans=[]
    for name,result in coin.items():
        if result!=0:
            ans.append([name,result])
    
    rename,re=ans[0][0],ans[0][1]
    for i in ans[1:]:
        if abs(i[1])>abs(re):
            rename,re=i[0],i[1]
    weigh=['light','heavy'][re>0]
    print(f'{rename} is the counterfeit coin and it is {weigh}.')

