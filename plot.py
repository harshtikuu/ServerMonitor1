import matplotlib.pyplot as plt
import readdata
import numpy as np
import sys
import csv
def format(string):
	return string[:-5]
def memoryplot(hostname):
	x,y=readdata.readmemory(hostname)
	x1,y1=[],[]
	for i,j in zip(x,y):
		if x.index(i)%2==0:
			x1.append(i)
		if y.index(j)%2!=0:
			y1.append(j)
	y=list(map(int,y1))
	x = list(np.arange(len(x1)))
	x1=list(map(format,x1))
	plt.xticks(x, x1)
	fig = plt.gcf()
	fig.subplots_adjust(bottom=0.3)
	plt.ylim(ymin=0,ymax=100)
	plt.title('Memory usage stats')
	plt.xlabel('time')
	plt.ylabel('percent used memory')
	plt.plot(x, y,label=hostname)
def diskplot(hostname):
	x,y=readdata.readdisk(hostname)
	x1,y1=[],[]
	for i,j in zip(x,y):
		if x.index(i)%2==0:
			x1.append(i)
		if y.index(j)%2!=0:
			y1.append(j)
	y=list(map(int,y1))
	x = list(np.arange(len(x1)))
	x1=list(map(format,x1))
	plt.xticks(x, x1)
	fig = plt.gcf()
	fig.subplots_adjust(bottom=0.2)
	plt.ylim(ymin=0,ymax=100)
	plt.title('Disk usage stats')
	plt.xlabel('time')
	plt.ylabel('percent used disk')
	plt.plot(x, y,label=hostname)
def cpuplot(hostname):
	x,y=readdata.readcpu(hostname)
	x1,y1=[],[]
	for i,j in zip(x,y):
		if x.index(i)%2==0:
			x1.append(i)
		if y.index(j)%2!=0:
			y1.append(j)
	y=list(map(float,y1))
	x = list(np.arange(len(x1)))
	x1=list(map(format,x1))
	plt.xticks(x, x1)
	fig = plt.gcf()
	fig.subplots_adjust(bottom=0.2)
	plt.ylim(ymin=0,ymax=100)
	plt.title('CPU usage stats')
	plt.xlabel('time')
	plt.ylabel('percent used CPU')
	plt.plot(x, y,label=hostname)

#plt.plot(x,y1)
#plt.show()
hostname=open('serverdata.csv','r+')
reader=csv.DictReader(hostname,delimiter=',')
if sys.argv[1]=='memory':
	for line in reader:
		memoryplot(line['hostname'])
elif sys.argv[1]=='disk':
	for line in reader:
		diskplot(line['hostname'])
elif sys.argv[1]=='cpu':
	for line in reader:
		cpuplot(line['hostname'])
else:
	print('Invalid argument')
plt.legend(loc='best')
plt.show()

'''
x,y=readdata.readdisk()
x1,y1=[],[]
for i,j in zip(x,y):
		if x.index(i)%2==0:
			x1.append(i)
		if y.index(j)%2!=0:
			y1.append(j)
y=list(map(int,y1))
'''

