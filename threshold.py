import csv
f=open('usagedata.csv','r+')
reader=csv.DictReader(f,delimiter=',')
def memorythreshold(hostname):
	f=open('usagedata.csv','r+')
    reader=csv.DictReader(f,delimiter=',')
	for line in reader:
		if line['hostname']==hostname:
			return int(line['memorythreshold'])
def cputhreshold(hostname):
	f=open('usagedata.csv','r+')
	reader=csv.DictReader(f,delimiter=',')
	for line in reader:
		if line['hostname']==hostname:
			return int(line['cputhreshold'])
def diskthreshold(hostname):
	f=open('usagedata.csv','r+')
	reader=csv.DictReader(f,delimiter=',')
	for line in reader:
		if line['hostname']==hostname:
			return int(line['diskthreshold'])

if __name__ == '__main__':
	print((diskthreshold('127.0.0.1')))
