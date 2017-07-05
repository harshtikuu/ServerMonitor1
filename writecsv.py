import csv
keys1 = ['time','memory']
keys2=['time','disk']
keys3=['time','cpu']
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
def cpuwrite(server):
	f=open('{}cpu'.format(server.hostname)+'.csv','a')
	writer=csv.DictWriter(f,keys3)
	writer.writerows(server.cpufile)

'''def downdata(server):
	f=open('downdata.csv','a')
	keys=['hostname','downpercentage']
	w=csv.DictWriter(f,keys1)
	w.writerows()'''
