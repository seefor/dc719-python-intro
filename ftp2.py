import socket
# the folowing will set our timeout socket connection to 2 seconds
socket.setdefaulttimeout(2)

#start a new socket connection
s = socket.socket()
s.connect(("172.16.180.130",21))
# we capture 1024 chare
banner = s.recv(1024)

if ("vsFTPd 2.3.4" in banner):
	print "[+] vsFTP Server is vulnerable."
elif ("3Com 3CDaemon FTP Server Version 2.0" in banner):
	print "[+] 3CDaemon FTP Server is vulnerable." 
elif ("Ability Server 2.34" in banner):
	print "[+] Ability FTP Server is vulnerable." 
elif ("Sami FTP Server 2.0.2" in banner):
	print "[+] Sami FTP Server is vulnerable."
else:
	print "[-] FTP Server is not vulnerable."