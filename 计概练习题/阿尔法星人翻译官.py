s=input()
ans=0
res=s
d={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,'hundred':100,'thousand':1000,'million':1000000}
if 'negative' in res:
    res=res[9:]
a=''
record=[]
for i in res:
    if i!=' ':
        a+=i
    else:
        record.append(d[a])
        a=''
record.append(d[a])
reans1,reans2=0,0
if 1000000 in record:
    record2=record[:record.index(1000000)]
    if 1000 in record2:
        record3=record2[:record.index(1000)]
        if 100 in record3:
            reans2+=100*sum(record3[:record3.index(100)])
            record3=record3[record3.index(100)+1:]
        reans1+=1000*(sum(record3)+reans2)
        record2=record2[record2.index(1000)+1:]
    if 100 in record2:
        reans1+=100*sum(record2[:record2.index(100)])
        record2=record2[record2.index(100)+1:]
    reans1+=sum(record2)
    ans+=1000000*reans1
    
    record=record[record.index(1000000)+1:]
reans=0
if 1000 in record:
    record2=record[:record.index(1000)]
    if 100 in record2:
        reans+=100*sum(record2[:record2.index(100)])
        record2=record2[record2.index(100)+1:]
    ans+=1000*(sum(record2)+reans)
    record=record[record.index(1000)+1:]
if 100 in record:
    ans+=100*sum(record[:record.index(100)])
    record=record[record.index(100)+1:]
ans+=sum(record)
print([ans,-ans]['negative' in s])
        
