import threading
import csv
import pxssh
import matplotlib.pyplot as plt
import time
import threshold
import mail
import math
import numpy
count=mail.getcount()
c1,c2=0,0
duration=mail.getduration()
currenttime1,currenttime2=time.time(),time.time()
mailsentdisc,mailsentmemory=False,False
class Server:
	def __init__(self,credentials):
		#threading.Thread.__init__(self)
		self.hostname=credentials['hostname']
		self.username=credentials['username']
		self.password=credentials['password']
		self.version= credentials['version']   
		self.s=pxssh.pxssh()
		self.memory=[]
		self.cpu=[]
		self.disk=[]
		self.y1=0
		self.y2=0
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
	def diskdata(self):
		hostname=self.hostname
		thresholdusage=threshold.diskthreshold(hostname)
		currentusage=self.disk[-1]
		string=''' Disk usage alert for {} \n
		 Current Disk usage = {}% \n Threshold = {}% \n Increase in limit = {}% 
		  '''.format(hostname,currentusage,thresholdusage,(currentusage- thresholdusage))
		return string
	def memorydata(self):
		hostname=self.hostname
		thresholdusage=threshold.memorythreshold(hostname)
		currentusage=self.memory[-1]
		string=''' Memory usage alert for {} \n
		 Current Memory usage = {}% \n Threshold = {}% \n Increase in limit = {}% 
		  '''.format(hostname,currentusage,thresholdusage,(currentusage- thresholdusage))
		return string


	def monitor(self):
		#self.cpumonitor()
		self.memorymonitor()
		global mailsentmemory,mailsentdisc,c1,c2,count,currenttime1,currenttime2,duration
		if threshold.memorythreshold(self.hostname)<self.memory[-1]:
			if  c2<count:
				if abs(time.time()-(currenttime1+duration*c2*60))<30:
					print('Sending memory alert to ',mail.maillist)
					mail.sendmessage(self.memorydata())
					c2+=1

		else:
			mailsentmemory=True
			#print('Memory usage above thresholds')
		self.diskmonitor()
		if threshold.diskthreshold(self.hostname)<self.disk[-1]:
			if  c1<count:
				if abs(time.time()-(currenttime2+duration*c1*60))<30:
					print('Sending disk alert to ',mail.maillist)
					try:
					 	mail.sendmessage(self.diskdata())
					except smtplib.SMTPAuthenticationError:
					 	print("Incorrect password,try again")
					c1+=1
		else:
			mailsentdisc=True
		time.sleep(0.1)		
	def start(self):
		while True:
			print('Monitoring ',self.hostname)
			self.monitor()
			#self.showval()
			
	def showval(self):
		self.y1+=1
		self.y2+=1
		figure(1)
		scatter(self.y1,self.memory)
		figure(2)
		scatter(self.y2,self.disk)
		pause(0.05)
		while True:
			pause(0.05)
if __name__ == '__main__':
	f=open('serverdata.csv','r+')
	reader=csv.DictReader(f,delimiter=',')
	objects=[Server(line) for line in reader]
	for thread in objects:
		thread.start()

