def is_runyear(n):
    if n%4!=0 or (n%100==0 and n%400!=0):
        return False
    else:
        return True
DAY=input()
n=int(input())
year=int(DAY[0:4])
month=int(DAY[5:7])
day=int(DAY[8:])
dic={1:31,2:[28,29],3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
while True:
    if n==0:
        break
    n-=1
    if month==2:
        day+=1
        if dic[2][is_runyear(year)]<day:
            day=1
            month+=1
    else:
        day+=1
        if dic[month]<day:
            day=1
            month+=1
            if month==13:
                month=1
                year+=1
print('%d-%02d-%02d'%(year,month,day))
print(f'{year}-{month:02}-{day:02}') 
print('{}-{:02}-{:02}'.format(year,month,day))  