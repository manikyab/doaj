import MySQLdb as sql
import csv

conn=sql.connect('localhost','root','','journal')
cur=conn.cursor()

csvfile1 = open('jlist.csv',encoding="utf8")

reader1 = csv.DictReader(csvfile1)
x=['Journal title','eISSN','Journal URL','pISSN','Publisher']
for row1 in reader:
    query1=("select * from doaj where EISSN=row1[x[1]] OR ISSN=row1[x[3]]")
    cur.execute(query1)
    check=cur.rowcount

    if check==0:

        query = ("insert into doaj""('Title','EISSN','URL','ISSN','Publisher','Add_Date')" "values('"+row1[x[0]]+"','"+row1[x[1]]+"','"+row1[x[2]]+"','"+row1[x[3]]+"','"+row1[x[4]]+"','"+row1[x[5]]+"')")
        query=query.encode("utf8")
        
        cur.execute(query) 
        conn.commit()

csvfile1.close()
cur.close()
conn.close()

