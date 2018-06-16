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
def voliss(a):
    try:
        b=a.cssselect("h2")
        #print(b)
        flag=0
        for i in range(len(b)):
            x=b[i].text_content()
            #print (x)
            if x[:4]=="VOL " or x[:4]=="Vol ":
                return x
        if flag==0:
            raise Exception("")
    except:
        b=a.cssselect("h3")
        print(b)
        for i in range(len(b)):
            x=b[i].text_content()
            #print(x)
            if x[:4]=="VOL " or x[:4]=="Vol ":
                return x
def vol(li,q1,q2,flag):
    #print(li)
    a=parse(li).getroot()
    b=a.cssselect("a")
    fl=0
    for i in b:
        x=i.text_content()
        if x[:4]=="VOL " or x[:4]=="Vol ":
            links=fl
        #print (fl)
        #print (x)
        fl+=1
    lin=b[links].get('href')
    #print(lin)
    c=parse(lin).getroot()
    d=c.cssselect("h2") #vol and Issue
    e=c.cssselect("td.tocPages") #Pages no
    z=voliss(c)
    #print(z)
    v=z[4:z.index(',')] #volume
    n=z[z.index(',')+5:z.index('(')-1] #issue
    x=c.cssselect("table.tocArticle")
    y=x[flag].cssselect("a")
    if len(y)==2:
        q1+='page,volume,issue,pdf_link,' #query creation
        q2+=e[flag].text_content()+"','"+v+"','"+n+"','"+y[1].get('href')+"','" #query creation
    else:
        q1+='page,volume,issue,' #query creation
        q2+=e[flag].text_content()+"','"+v+"','"+n+"','" #query creation
    q1=q1[:-1]
    q2=q2[:-2]
    query=q1+q2+")"
    return query
conn=sql.connect("192.168.1.48","python","python","journal")
cur=conn.cursor()
flag=0
cur.execute("select * from link") 
z=cur.fetchall()
link=z[-1][0]
if link[-2:]=="\n":
    link=link[:-2]
#link=input("Link of RSS feed:")
#link=sys.argv[1]
#print (link)
a=fd.parse(link)
y=a['items']
#print (y)
z=['title','link','summary','published','author']
x=list(y[0].keys())
#print ()
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
    #print (flag)
    flag+=1
    query=query.encode("utf-8")
    cur.execute(query)
    conn.commit()
cur.close()
conn.close()
print (flag," entries inserted.")
