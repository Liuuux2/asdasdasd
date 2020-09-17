#/usr/bin/python
import socket
header = ('Tumama es tanga')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.settimeout(1)
s.connect(('209.222.97.89', 25565))
s.send(header)
s.close() 
