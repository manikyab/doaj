import csv
z=['Journal title','Journal EISSN (online version)','Journal URL','Alternative title','Journal ISSN (print version)','Publisher','Society or institution','Platform, host or aggregator','Country of publisher','Full text formats','Keywords','Full text language','Added on Date','Subjects']
with open('doaj_20180604_0530_utf8.csv','rb') as csvfile:
	
 reader = csv.DictReader(csvfile)
 for row in reader:
 	for d in z:
 		print row[d]+'\t',
 	print 
