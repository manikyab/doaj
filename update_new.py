import urllib.request
import csv
import os
import feedparser as fd
import update_entry
import time
import datetime
def findissn(tit):
	y=tit[::-1]
	z=y.index("(")
	x=[]
	if(z==21):
		x.append(tit[:-24])
		x.append(tit[-21:-12])
		x.append(tit[-10:-1])
	else:
		x.append(tit[:-12])
		x.append(tit[-10:-1])
	return x

def matchissn(x,je,ji):
	y=len(x)
	temp=[]
	if y==2:
		if x[1] in je:
			temp.append(je.index(x[1]))
			temp.append('je')
		else:
			temp.append(ji.index(x[1]))
			temp.append("ji")
		return temp
	else:
		if x[1] in je:
			temp.append(je.index(x[1]))
			temp.append('je')
		else:
			temp.append(ji.index(x[1]))
			temp.append("ji")
		return temp
def sleep(t):
	time.sleep((60*30)-t)
while True:
	t1=datetime.datetime.now()
	os.remove("data.csv")
	urllib.request.urlretrieve ("https://doaj.org/csv", "data.csv")
	j=['Journal title','Journal EISSN (online version)','Journal URL','Journal ISSN (print version)','Added on Date']
	jt=[]
	je=[]
	ji=[]
	ju=[]
	jd=[]
	csvfile=open('doaj_20180604_0530_utf8.csv','rb')
	reader = csv.DictReader(csvfile)
	for row in reader:
		jt.append(row[j[0]])
		je.append(row[j[1]])
		ju.append(row[j[2]])
		ji.append(row[j[3]])
		jd.append(row[j[4]])
	a=fd.parse("https://doaj.org/feed")
	y=a['items']
	new=dict()
	for i in y:
    	au=i['author']
    	ca=i['category']
    	con=i['content'][0]['src']
    	linka=i['links'][0]['href']
    	linkr=i['links'][1]['href']
    	suma=i['content'][1]['value']
    	tit=i['title']
    	upd=i['updated']
    	id=i['id']
    	x=findissn(tit)
    	ind=matchissn(x,je,ji)
    	update_entry.insert_data(ind,x[1])
    t2=datetime.datetime.now()
    t3=t2-t1
    t3=int(t3.total_seconds())
    sleep(t3)

