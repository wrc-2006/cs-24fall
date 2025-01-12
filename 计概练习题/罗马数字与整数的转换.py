s=input()
lst1=[0,1,2,3,4,5,6,7,8,9]
lst2=['','I','II','III','IV','V','VI','VII','VIII','IX']
if s[0] in [str(i) for i in range(0,10)]:
    t=int(s)
    new_s=''
    num_M=t//1000
    t%=1000
    new_s+='M'*num_M
    num_bai=t//100
    if num_bai in [4,9]:
        new_s+=['CD','CM'][num_bai==9]
    else:
        m=100*t//100
        if m>=500:
            new_s=new_s+'D'+'C'*((m-500)//100)
        else:
            new_s+='C'*(m//100)
    t%=100
    num_shi=t//10
    if num_shi in [4,9]:
        new_s+=['XL','XC'][num_shi==9]
    else:
        n=10*t//10
        if n>=50:
            new_s=new_s+'L'+'X'*((n-50)//10)
        else:
            new_s+='X'*(n//10)
    t%=10
    new_s+=lst2[lst1.index(t)]
    print(new_s)
else:
    newnum=0
    lst3=['I','V','X','L','C','D','M']
    lst4=[1,5,10,50,100,500,1000]
    newlst=[]
    for i in s:
        newlst.append(lst4[lst3.index(i)])
    for i in range(len(newlst)-1):
        if newlst[i]>=newlst[i+1]:
            newnum+=newlst[i]
        else:
            newnum=newnum-newlst[i]
    newnum+=lst4[lst3.index(s[-1])]
    print(newnum)