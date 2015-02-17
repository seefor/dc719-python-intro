import socket
socket.setdefaulttimeout(2)
s = socket.socket()
try:
        s.connect(("172.16.180.130",21))
        ans = s.recv(1024)
        print ans
except Exception, e:
        print "[-] Error = "+str(e)