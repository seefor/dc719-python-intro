import socket
import argparse
__author__ = 'Sif Baksh taken from Violent Python by TJ. O\'Connor'
 
parser = argparse.ArgumentParser(description='This is a demo script by Sif Baksh.')
parser.add_argument('-i','--i',help='Use -i 10.10.10.', required=True)
args = parser.parse_args()

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except Exception, e:
		print "[-] "+ ip + " Error : "+str(e)

def checkVulns(banner,ip):
	if ("FreeFloat Ftp Server (Version 1.00)" in banner):
		print "[+] FreeFloat FTP Server is vulnerable."
	elif ("(vsFTPd 2.3.4)" in banner):
		print "[+] "+ ip + " Found : vsFTPd 2.3.4 is vulnerable."
	else:
		print "[-] FTP Server is not vulnerable."
	return
	
def main():
	port = 21
	for x in range (124,131):
		banner1 = retBanner(args.i+str(x), port)
		if banner1:
			checkVulns(banner1,args.i+str(x))
			
if __name__ == '__main__':
	main()