import pxssh
def isdown(server):
	server.s.sendline('ping -c 3 {} | grep transmitted'.format(server.hostname))
	server.s.prompt()
	loss=int(str(server.s.before)[str(server.s.before).find('%')-1])
	if loss==0:
		return False
	elif loss==100:
		return True
