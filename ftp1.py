import socket
# the folowing will set our timeout socket connection to 2 seconds
socket.setdefaulttimeout(2)

#start a new socket connection
s = socket.socket()
try:
        s.connect(("172.16.180.130",21))
	# we capture 1024 chare
        ans = s.recv(1024)
        print ans
except Exception, e:
        print "[-] Error = "+str(e)
