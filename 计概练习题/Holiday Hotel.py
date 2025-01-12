'''
while True:
    n=int(input())
    if n==0:
        break
    s=[]
    for _ in range(n):
        d,c=[int(x) for x in input().split()]
        s.append([d,c])
    num=0
    p=n
    while p!=0:
        p-=1
        s.append(s.pop(0))
        for i in s[1:]:
            if i[0]<s[0][0] and i[1]<=s[0][1]:
                break
            if i[1]<s[0][1] and i[0]<=s[0][0]:
                break
        else:
            num+=1
    print(num)
'''    
###已经习惯的TLE，虽然这是我40分钟才编出来的代码呜呜呜

#题中两个要求是逆否命题
while True:
    n=int(input())
    if n==0:
        break
    s=[]
    for _ in range(n):
        d,c=[int(x) for x in input().split()]
        s.append([d,c])
    s.sort(key=lambda x:(x[0],x[1]))   #第二个元素应该按升序排，即d相同的酒店最多只能有一个候选
    hotel=n
    for i in s[1:]:
        if s[0][1]<=i[1]:
            hotel-=1
            continue
        s[0][1]=i[1]
    print(hotel)
    
    
    
            
