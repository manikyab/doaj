import feedparser as fd
import csv
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