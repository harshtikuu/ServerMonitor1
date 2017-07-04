import csv
import sys
def readmemory(hostname):
	try:
		f=open('{}mem'.format(hostname)+'.csv','r+')
	except:
		print('No memory stats found for {}'.format(hostname))
		sys.exit(1)
	reader=csv.DictReader(f,delimiter=',')
	reader=list(reader)
	x=[]
	y=[]
	for line in reader:
		x.append(line['time'])
		y.append(line['memory'])
	return x,y
def readdisk(hostname):
	try:
		f=open('{}disk'.format(hostname)+'.csv','r+')
	except:
		print('No memory stats found for {}'.format(hostname))
	reader=csv.DictReader(f,delimiter=',')
	reader=list(reader)
	x=[]
	y=[]
	for line in reader:
		x.append(line['time'])
		y.append(line['disk'])
	return x,y

if __name__ == '__main__':
		print(readdisk())		

	
