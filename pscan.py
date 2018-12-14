#!/usr/bin/python3
"""
a python based scanner
author- VeeKay
last modified on 06/08/18 4:48 pm


"""

import socket
import sys
import time
def getBanner(ip, port):
	try:
		socket.setdefaulttimeout(1)
		s=socket.socket()
		s.connect((ip,int(port)))
		banner=s.recv(1024)
		return banner
	except :
		return
iph = "172.16.10."
if len(sys.argv)==2:
	st=sys.argv[1]
else:
	st=input("Enter your range and port (i.e. 201-223:22): ")
r1=int(st.split("-")[0])
r2=int(st.split("-")[1].split(":")[0])
try:
	port=st.split("-")[1].split(":")[1]
except:
	port="22"
ctime=time.strftime('%d/%m/%Y %H:%M:%S')
slog = open("pscan.log","a")
slog.write("\n\n"+ctime+"\n\n")
for i in range(r1,r2+1):
	print("trying "+iph+str(i)+":"+port+"...")
	banner1=getBanner(iph+str(i),port)
	if banner1:
		print(iph+str(i)+" "+str(banner1))
		slog.write("[+] "+iph+str(i)+":"+port+" open\n")
slog.close()
