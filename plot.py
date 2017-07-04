import matplotlib.pyplot as plt
import readdata
import numpy as np
import sys
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
	plt.scatter(x, y)
	plt.show()
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
	plt.plot(x, y)
	plt.show()
#plt.plot(x,y1)
#plt.show()
hostname=input('Enter hostname')
if sys.argv[1]=='memory':
	memoryplot(hostname)
elif sys.argv[1]=='disk':
	diskplot(hostname)
else:
	print('Invalid argument')


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

