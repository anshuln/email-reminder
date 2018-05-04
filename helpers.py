'''
Contains random helper functions
'''
def getdate():
    from datetime import date
    from datetime import timedelta
    day=timedelta(days=1)
    today=date.today()- 0*day  
    strday=str(today)
    buff=strday.split('-')
    chart=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
    mon=chart[int(buff[1])-1]
    dat=buff[2]+'-'+mon+'-'+buff[0]
    dat="SINCE "+dat
    return dat
def std_date():
    
    buff=getdate().split()[1]
    day=buff.split('-')[0]
    mon=buff.split('-')[1][:3]
    #print(day+' '+mon)
    return day+' '+mon

today=std_date()

def compare_date(d1,d2):
    chart={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    d_1=d1.split()
    d_2=d2.split()
    #print(d_1)
    #print(d_2)
    
    if(len(d_1)>1 and len(d_2)>1):
        if(chart[d_1[1]]>chart[d_2[1]]):
            return 1
        elif(chart[d_1[1]]<chart[d_2[1]]):
            return -1
        else:
            if(d_1[0]>d_2[0]):
                return 1
            elif(d_1[0]<d_2[0]):
                return -1
            else:
                return 0
    else:
        return 0        
def key(l1,l2):
    d1=l1[1].split('-')[1]
    d2=l2[1].split('-')[1]
    return compare_date(d1,d2)

def no_dup(lis):
    new_list=[]
    for j in lis:
        if j not in new_list:
            new_list.append(j)
    return new_list
