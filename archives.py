import feedparser as fd
from lxml.html import parse

def clean(text):
	text=text.replace('\n','')
	text=text.replace('\t','')
	return text
def test(x,q):
        if "Keywords" in x:
                temp=x.split("Keywords: ")
                q['summary']=temp[0]
                q['keyword']=temp[1]
                return q
        else:
                q['summary']=x
                return q
def abstract(link,q):
	a=parse(link).getroot()
	b=a.get_element_by_id('articleAbstract')
	x=b.text_content()
	x=clean(x)
	x=x[8:]
	return test(x,q)
def data(issue_link,q):
	a=parse(issue_link).getroot()
	b=a.cssselect('table.tocArticle')
	qw=q
	for i in b:
		c=i.cssselect('a')
		d=i.cssselect('td.tocTitle')
		e=i.cssselect('td.tocAuthors')
		f=i.cssselect('td.tocPages')
		q['title']=clean(d[0].text_content())
		q['author']=clean(e[0].text_content())
		q['page']=clean(f[0].text_content())
		q['link']=c[0].get('href')
		q=abstract(q['link'],q)
		if len(c)==2:
			q['pdf_link']=c[1].get('href')
		q_print(q)
		q=qw



def q_print(q):
        q1="insert into article("
        q2=") values('"
        y=list(q.keys())
        for i in y:
                q1=q1+i+","
                q2=q2+q[i]+"','"
        q1=q1[:-1]
        q2=q2[:-2]+")"
        query=q1+q2
        print(query)
link=input("Link of RSS feed:")
qd=dict()
a=fd.parse(link)
j_link=a['feed']['link']
qd['j_link']=j_link
j_name=a['feed']['title']
qd['j_title']=j_name
qd['lang']=a['feed']['language']
jou=parse(j_link).getroot()
b=jou.cssselect('a')
flag=0
for i in b:
	x=i.text_content()
	if x=='Archives':
		fl=flag
		break
	flag+=1
arc_link=b[fl].get('href')
print(arc_link)
arc=parse(arc_link).getroot()
iss=arc.cssselect("a")
for i in iss:
	x=i.text_content()
	q=qd
	if 'Vol ' in x:
		link=i.get('href')
		q['volume']=x[4:x.index(',')] #volume
		q['issue']=x[x.index(',')+5:x.index('(')-1]
		q=data(link,q)
		print (q)

