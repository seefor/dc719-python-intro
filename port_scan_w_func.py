import socket
def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except Exception, e:
		print "[-] "+ ip + " Error : "+str(e)


def main():
	port = 21
	for x in range (24,32):
		banner1 = retBanner("172.16.180.1"+str(x), port)
		if banner1:
			print '[+] 172.16.180.1' + str(x) + ' Found : ' + banner1
	
if __name__ == '__main__':
	main()