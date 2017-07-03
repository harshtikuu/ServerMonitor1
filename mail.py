import yagmail
import csv
import getpass
f=open('mail.csv','r+')
reader=csv.DictReader(f,delimiter=',')
password=getpass.getpass()
maillist=[]
for line in reader:
	maillist.append(line['mails'])
def getcount():
	return int(line['number'])
def getduration():
	return int(line['duration'])
def sendmessage(message):
	yag=yagmail.SMTP('tiku.harsh',password)
	yag.send(maillist,'alert',message)

if __name__=="__main__":
	sendmessage('message')