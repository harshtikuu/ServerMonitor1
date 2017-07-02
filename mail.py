import yagmail
import csv
f=open('mail.csv','r+')
reader=csv.DictReader(f,delimiter=',')
maillist=[]
for line in reader:
	maillist.append(line['mails'])
def sendmessage(message):
	yag=yagmail.SMTP('tiku.harsh','tensorflow')
	yag.send(maillist,'alert',message)

if __name__=="__main__":
	sendmessage('shit is working bro')