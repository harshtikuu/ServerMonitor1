import csv
f=open('serverdata.csv','r+')
reader=csv.DictReader(f,delimiter=',')
for line in reader:
	f=open('{}mem'.format(line['hostname'])+'.csv','a')
	f.write('time,memory\n')
	f.close()
	f=open('{}disk'.format(line['hostname'])+'.csv','a')
	f.write('time,disk\n')
	f.close()
