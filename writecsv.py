import csv
keys1 = ['time','memory']
keys2=['time','disk']
def writeheader(server):
	f=open('{}mem'.format(server.hostname)+'.csv', 'a')
	w=csv.DictWriter(f,keys1)
	w.writeheader()
	f.close()
	f=open('{}disk'.format(server.hostname)+'.csv','a')
	w=csv.DictWriter(f,keys2)
	w.writeheader()
def memorywrite(server):
	f=open('{}mem'.format(server.hostname)+'.csv', 'a')
	writer=csv.DictWriter(f,keys1)
	writer.writerows(server.memoryfile)
def diskwrite(server):
	f=open('{}disk'.format(server.hostname)+'.csv','a')
	writer=csv.DictWriter(f,keys2)
	writer.writerows(server.diskfile)