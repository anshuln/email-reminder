import re 
date=re.compile(r'\b((\d{1,2})(th|st|\s|rd)\s?(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec))|((\d{1,2})(/|-)(\d{1,2})(/|-)(\d{2,4}))|((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec).*\d{1,2})',re.I)  #use res[0][0] as actual date
time=re.compile(r'\s(([0-1][0-9](00|15|30|45|59))|([2][0-4](00|15|30|45|59)))|(\d{1,2}(\.|\:|\s?)(\d{2})?\s?(A(\.?)M(\.?)|P(\.?)M(\.?)))',re.I)
brackets=re.compile(r'\[.*\]')
hit_list=re.compile(r'(reminder|call|book)',re.IGNORECASE)
venue=re.compile(r'(where|venue|place)\s?(\:|\-)\s?(\S*\s){1,3}',re.IGNORECASE)
reg=re.compile(r'\bregist',re.IGNORECASE)
link=re.compile(r'https\:\/\/.*\s')

def purify_date(text):
	buff=text.split()
	day=re.split(r'st|th|rd',buff[0])[0]
	if(len(day)==1):
		day='0'+day		#you have handled only one type of date
	month=buff[1][:3]
	print(day)
	pure_date=day+' '+month
	return pure_date
def clean_up(text):				#gives a readable mail
       
    begin=re.compile(r'\={40}')
    buff=re.split(begin,text)
    text=buff[len(buff)-1]
    end=re.compile(r'\n(Best\s)?Regards',re.IGNORECASE)
    buff=re.split(end,text)
    text=buff[0]
    end=re.compile(r'(\n(for).*contact)?',re.IGNORECASE)				#quoted mails might cause
    buff=re.split(end,text)
    text=buff[0]  
    return text
def get_date(text):
	dates=re.findall(date,text)
	#print("Dates:")
	date_ret=set([])
	for index in dates:
		if(len(index[0])):
			date_ret.add(purify_date(index[0]))
	return(date_ret)


'''def get_time(text):
	times=re.findall(time,text)
	for index in times:
        if(len(index[0])):
            print(index[0])
        if(len(index[5])):
            print(index[5])'''
def get_time(text):
    times=re.findall(time,text)
    #print("Timings")
    time_ret=set([])
    for index in times:
        if(len(index[0])):
            time_ret.add(index[0])
        elif(len(index[5])):
            time_ret.add(index[5])
    return(time_ret)
def get_title(text):
	while(re.match(brackets,text)):
		text=re.split(brackets,text)[1]
	text=text.split('|')[0]
	if(re.search(hit_list,text)):
		return ''				#check length of text in main()
	return (text)
def get_venue(text):
	venues=re.search(venue,text)
	if venues:
		ret=venues.group()
		ven=re.compile(r'(where|venue|place)\s?(\:|\-)\s?',re.IGNORECASE)
		buff=re.split(ven,ret)
		ret=buff[3]
		return ret
	else:
		return ''
def check_reg(text):
	if(re.search(reg,text)):
		return 'Yes'
	return 'No'
def get_links(text):
	ret=[]
	links=re.findall(link,text)
	for index in links:
		ret.append(index)
	return ret
