import csv
import helpers
import os

def check():
	file=open('Database.csv')
	reader=csv.reader(file)
	data=list(reader)
	for row in range(1,len(data)):
		dates=data[row][1].split('-')
		for dat in dates:
			if(len(dat)>1):
				print(dat+" "+helpers.today+" "+str(helpers.compare_date(dat,helpers.today)))
				if(helpers.compare_date(dat,helpers.today)==0):
					if(data[row][6]=='1'):
						print("You have an upcoming event today:- ",data[row][0])
def add():
	import email_integration
	add_this=email_integration.get_data()
	#file=open('Database.csv', 'a', newline='')
	file=open('Database.csv','a',newline='')
	writer = csv.writer(file)

	for index in add_this:
		addition=[]
		addition.append(index.title)
		app_date=''
		for date in index.dates:
			
			app_date=app_date+date
			if(len(app_date)>0):
				app_date=app_date+'-'
		addition.append(app_date)
		app_date=''
		for time in index.times:
			
			app_date=app_date+time
			app_date=app_date+'-'
		addition.append(app_date)
		addition.append(index.venue)
		links=''
		for link in index.links:
			links=links+' , '
			links=links+link
		addition.append(links)
		addition.append(index.reg)
		print(index.title)
		addition.append('0')		#going or not
		writer.writerow(addition)
	file.close()
def manage():
	rfile=open('Database.csv')
	reader=csv.reader(rfile)
	data=list(reader)
	write_in=[]
	flag=0
	for row in range(1,len(data)):
		dates=data[row][1].split('-')
		for dat in dates:
			
			if(len(dat)>=1):
				
				if(helpers.compare_date(helpers.today,dat)<=0):
					write_in.append(data[row])
					flag=1
			if flag==1:
				break		
	#write_in=sorted(write_in,key=helpers.key)
	#print("Before")
	#print(len(write_in))
	write_in=helpers.no_dup(write_in)
	#print("After")
	#print(len(write_in))
	rfile.close()
	wfile=open('buff.csv','w+',newline='')
	writer=csv.writer(wfile)
	writer.writerow(['Title','Dates','Timings','Venue','Links','Registrations?','Going?'])
	for row in range(len(write_in)):
		writer.writerow(write_in[row])
	os.remove("Database.csv")
	
	wfile.close()
	os.rename("buff.csv","Database.csv")
def main():
	add()
	check()
	manage()
	
	
		



