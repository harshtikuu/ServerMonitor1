import csv
import os
f=open('serverdata.csv','r+')
reader=csv.DictReader(f,delimiter=',')
for line in reader:
	if not os.path.isfile('{}mem'.format(line['hostname'])+'.csv'):
		f=open('{}mem'.format(line['hostname'])+'.csv','a')
		f.write('time,memory\n')
		f.close()
	if not os.path.isfile('{}disk'.format(line['hostname'])+'.csv'):
		f=open('{}disk'.format(line['hostname'])+'.csv','a')
		f.write('time,disk\n')
		f.close()
