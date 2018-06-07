def insert(ind,x)
    import MySQLdb as sql
    import csv

    def quotes(row):
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

    conn=sql.connect('localhost','root','','journal')
    cur=conn.cursor()
    if ind[1]=='je':
        cur.execute("select * from doaj where EISSN=x")
        check=cur.rowcount
    else:
        cur.execute("select * from doaj where ISSN=x")
        check=cur.rowcount

    if check==0:
        z=['Journal title','Journal EISSN (online version)','Journal URL','Alternative title','Journal ISSN (print version)','Publisher','Society or institution','Platform, host or aggregator','Country of publisher','Full text formats','Keywords','Full text language','First calendar year journal provided online Open Access content','Added on Date','Subjects'] #attributes 

        csvfile = open('data.csv',encoding="utf8") #open the file with binary encoding
            
        reader = csv.DictReader(csvfile) #iterating line by line from the data.csv
    
        row=reader[ind[0]]
        row=quotes(row)    

        date=row[z[13]]
        query = "insert into doaj values('"+row[z[0]]+"','"+row[z[1]]+"','"+row[z[2]]+"','"+row[z[3]]+"','"+row[z[4]]+"','"+row[z[5]]+"','"+row[z[6]]+"','"+row[z[7]]+"','"+row[z[8]]+"','"+row[z[9]]+"','"+row[z[10]]+"','"+row[z[11]]+"','"+row[z[12]]+"','"+date[0:10]+"','"+row[z[14]]+"')"
        query=query.encode("utf8")
        
        cur.execute(query) 
        conn.commit()
       
        
    csvfile.close()
    cur.close()
    conn.close()