import urllib
import csv
import os
import feedparser as fd
def findissn(tit):
	y=tit[::-1]
	z=y.index("(")
	x=[]
	if(z==21):
		x.append(tit[:-24])
		x.append(tit[-21:-12])
		x.append(tit[-10:-1])
	else:
		x.append(tit[:-13])
		x.append(tit[-10:-1])
	return x

os.remove("data.csv")
urllib.urlretrieve ("https://doaj.org/csv", "data.csv")
z=['Journal title','Journal EISSN (online version)','Journal URL','Journal ISSN (print version)','Added on Date']
jt=[]
je=[]
ji=[]
ju=[]
jd=[]
csvfile=open('doaj_20180604_0530_utf8.csv','rb')
reader = csv.DictReader(csvfile)
for row in reader:
	jt.append(row[z[0]])
	je.append(row[z[1]])
	ji.append(row[z[2]])
	ju.append(row[z[3]])
	jd.append(row[z[4]])
a=fd.parse("https://doaj.org/feed")
y=a['items']
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