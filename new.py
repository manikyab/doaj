import feedparser as fd

a= fd.parse("https://doaj.org/feed")
x=a['items']
for j in x:
	at=j['author']
	cat=j['category']
	con=j['content']
	print at