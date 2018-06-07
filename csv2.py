import csv

# store all the feeds in the csvfile
z=['Journal title','Journal EISSN (online version)','Journal URL','Alternative title','Journal ISSN (print version)','Publisher','Society or institution','Platform, host or aggregator','Country of publisher','Full text formats','Keywords','Full text language','Added on Date','Subjects']
with open('doaj_20180604_0530_utf8.csv','rb') as csvfile

# read a csv file using DictReader
 reader = csv.DictReader(csvfile)
	
#for printing the details
 for row in reader:
 	for d in z:
 		print row[d]+'\t',
 	print 
