#python 3

import MySQLdb as sql
import csv 
import urllib.request


conn=sql.connect('localhost','root','','journal')
cur=conn.cursor()

urllib.request.urlretrieve ("https://doaj.org/csv", "data.csv") #saving doaj_db file in data.csv
z=['Journal title','Journal EISSN (online version)','Journal URL','Alternative title','Journal ISSN (print version)','Publisher','Society or institution','Platform, host or aggregator','Country of publisher','Full text formats','Keywords','Full text language','Added on Date','Subjects'] #attributes 

csvfile = open('data.csv',encoding="utf8") #open the file with binary encoding
	
reader = csv.DictReader(csvfile) #iterating line by line from the data.csv
for row in reader:
    
    #title=row[z[0]]
    #eissn=row[z[1]]
    #url=row[z[2]]
    #alt_title=row[z[3]]
    #issn=row[z[4]]
    #publisher=row[z[5]]
    #institute=row[z[6]]
    #host=row[z[7]]
    #country=row[z[8]]
    #formats=row[z[9]]
    #keyword=row[z[10]]
    #language=row[z[11]]
    #date=row[z[12]]
    #sunject=row[z[13]]

    cur.execute("insert into doaj values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,)",(row[z[0]],row[z[1]],row[z[2]],row[z[3]],row[z[4]],row[z[5]],row[z[6]],row[z[7]],row[z[8]],row[z[9]],row[z[10]],row[z[11]],row[z[12]],row[z[13]],)) 
          
csvfile.close()
cur.close()
conn.close()
