pig=[]
ans=[]
while True:
    try:
        s=input()
        if len(s)>4:
            n=int(s[5:])
            pig.append(n)
            if not ans:
                ans.append(n)
            else:
                ans.append(min(n,ans[-1]))    ##加入n和最后一个数当中较小的一个，既确保
        if s=='pop':                          ##ans中猪的数量与pig中一致，也使最后一个为最小值
            if len(pig)>0:
                pig.pop()
                ans.pop()
        if s=='min':
            if len(pig)>0:
                print(ans[-1])
    except EOFError:
        break
    