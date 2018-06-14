import feedparser as fd
import MySQLdb as sql
from lxml.html import parse

def quotes(row,z):
    for i in z:
        c=row[i].count("'")
        if c!=0:
            temp=row[i].split("'")
            emp=temp[0]
            for j in temp[1:]:
                emp=emp+"''"
                emp=emp+j
            row[i]=emp
    return row

def vol(li,q1,q2,flag):
    #print(li)
    a=parse(li).getroot()
    b=a.cssselect("a")
    lin=b[21].get('href')
    #print(lin)
    c=parse(lin).getroot()
    d=c.cssselect("h2") #vol and Issue
    e=c.cssselect("td.tocPages") #Pages no
    f=c.cssselect("a.file") #PDF link
    try:
        z=d[0].text_content() #volume and issue data
    except:
        d=c.cssselect("h3")
        z=d[0].text_content()
    v=z[4:z.index(',')] #volume
    n=z[z.index(',')+5:z.index('(')-1] #issue
    q1+='page,volume,issue,pdf_link,' #query creation
    q2+=e[flag].text_content()+"','"+v+"','"+n+"','"+f[flag].get('href')+"','" #query creation
    q1=q1[:-1]
    q2=q2[:-2]
    query=q1+q2+")"
    return query
conn=sql.connect("192.168.1.48","python","python","journal")
cur=conn.cursor()
flag=0
link=input("Link of RSS feed:")
a=fd.parse(link)
y=a['items']
z=['title','link','summary','published','author']
x=list(y[0].keys())
temp=list(set(z) & set(x))
lang=a['feed']['language']
j_title=a['feed']['title']
j_link=a['feed']['link']
for i in y:
    q1="insert into article(lang,j_title,j_link,"
    q2=") values('"+lang+"','"+j_title+"','"+j_link+"','"
    i=quotes(i,temp)
    for j in temp:
        q1+=j+','
        q2+=i[j]+"','"
    
    query=vol(i['link'],q1,q2,flag)
    #print(query)
    print (flag)
    flag+=1
    query=query.encode("utf-8")
    cur.execute(query)
    conn.commit()
cur.close()
conn.close()
	
