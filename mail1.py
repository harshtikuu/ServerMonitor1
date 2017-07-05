import smtplib
import csv
import getpass
import sys
f=open('mail.csv','r+')
reader=csv.DictReader(f,delimiter=',')
maillist=[]
for line in reader:
	maillist.append(line['mails'])
def getcount():
	return int(line['number'])
def getduration():
	return int(line['duration'])
def sendmessage(message):
	try:
		yag=smtplib.SMTP('192.168.1.101:25')
		yag.sendmail('intern.harsh@lavainternational.in',maillist,message)
	except :
		print('Cannot login: \n Possible Reasons: \n 1. No network connection. \n 2.Cannot connect to relay server')
		sys.exit(1)
	

if __name__=="__main__":
	sendmessage('message')