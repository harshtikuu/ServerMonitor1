import threading
import csv
import pxssh
from matplotlib.pyplot import *
import time
import threshold
import warning
import mail,numpy
mailsentmemory=False
mailsentdisc=False
class Server(threading.Thread):
	def __init__(self,credentials):
		threading.Thread.__init__(self)
		self.hostname=credentials['hostname']
		self.username=credentials['username']
		self.password=credentials['password']
		self.version= credentials['version']   
		self.s=pxssh.pxssh()
		self.memory=[]
		self.cpu=[]
		self.disk=[]
		self.s.login(self.hostname,self.username,self.password)
	def memorymonitor(self):
		if self.version=='rhel7':
			self.s.sendline(''' awk '/^Mem/ {printf("%u%%", ($4/$2)*100);}' <(free -m) ''')
		else:
			self.s.sendline(''' awk '/^Mem/ {printf("%u%%", ($4/$2)*100);}' <(free -m) ''')
		self.s.prompt()
		self.memory.append((int(self.s.before[-3:-1])))
	#def cpumonitor(self):
	##	self.s.prompt()
	#	sendlinelf.cpu.append((int(self.s.before[-3:-1]))) 
	def diskmonitor(self):
		self.s.sendline(''' awk '/^total/ {printf("%u%%", $5);}' <(df -h --total) ''')
		self.s.prompt()
		self.disk.append((int(self.s.before[-3:-1])))

	def monitor(self):
		#self.cpumonitor()
		self.memorymonitor()
		global mailsentmemory
		if threshold.memorythreshold(self.hostname)<self.memory[-1]:
			if  not mailsentmemory:
				mail.sendmessage(warning.memorywarning())
				mailsentmemory=True
		else:
			mailsentmemory=False
		self.diskmonitor()
		if threshold.diskthreshold(self.hostname)<self.disk[-1]:
			if not mailsentdisc:
				mail.sendmail(warning.diskwarning())
				mailsentdisc=True
		else:
			mailsentdisc=False
		time.sleep(1)		
	def run(self):
		while True:
			self.monitor()
	def showval(self):
		y1=[].append(numpy.random.random())
		y2=[].append(numpy.random.random())
		figure(1)
		plot(y1,self.memory)
		figure(2)
		plot(y1,self.disk)
		show()
f=open('serverdata.csv','r+')
reader=csv.DictReader(f,delimiter=',')
objects=[Server(line) for line in reader]
for thread in objects:
	thread.start()
#thread.showval()
