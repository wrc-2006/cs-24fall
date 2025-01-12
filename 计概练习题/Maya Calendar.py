n=int(input())
print(n)
lst_hmonth=['pop','no','zip','zotz','tzec','xul','yoxkin','mol','chen','yax','zac','ceh','mac','kankin','muan','pax','koyab','cumhu']
lst_t2=['imix','ik','akbal','kan','chicchan','cimi','manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib','caban','eznab','canac','ahau']
lst_t1=[x for x in range(1,14)]
for _ in range(n):
    hday,hmonth,hyear=[x for x in input().split()]
    hday=int(hday[:-1])
    hyear=int(hyear)
    if hmonth=='uayet':
        day=360+hday+1+365*hyear
    else:
        day=20*lst_hmonth.index(hmonth)+hday+1+365*hyear
    tyear=day//260
    if day%260==0:
        tyear-=1
    day%=260
    tday2=lst_t2[day%20-1]
    tday1=lst_t1[day%13-1]
    print(f'{tday1} {tday2} {tyear}')