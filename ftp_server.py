#-*- coding: UTF-8 -*-
import os
import time
import socket

def server():
	IP_PORT=('0.0.0.0',9999)
	sk=socket.socket()
	sk.bind(IP_PORT)
	sk.listen(5)
 
	BASE_DIR=os.path.dirname(os.path.abspath(__file__))

	print("server is started, waitting for connection...")

	while True:
		conn,addr=sk.accept()

		print("{0},{1} connected".format(addr[0],addr[1]))
		while True:
			data=conn.recv(1024)
			cmd,filename,file_size=str(data).split('|')

			path=os.path.join(BASE_DIR,'data',filename)
			file_size=int(file_size)

			has_sent=0

			with open(path,'wb') as fp:
				while has_sent!=file_size:
					data=conn.recv(1024)
					fp.write(data)

					has_sent+=len(data)
					#print('\r'+'[progress]:%s.02f%%'%('>'*int((has_sent/file_size)*50),float(has_sent/file_size)*100),end='')
			print()
			print("%s ok"%filename)
if __name__=="__main__":
	server()