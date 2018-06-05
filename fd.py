#for python 2.7 edit for python 3

import feedparser as fd
import MySQLdb as sql
a=fd.parse("https://doaj.org/feed")
conn=sql.connect('localhost','root','','journal')
cur=conn.cursor()
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
    query="insert into doaj values('"+au+"','"+ca+"','"+con+"','"+linka+"','"+linkr+"','"+suma+"','"+tit+"','"+upd+"','"+id+"')"
    cur.execute(query)
    print cur.fetchone()
    #print query
