#-*- coding: UTF-8 -*-
import os
import time
import socket

def client():
    IP_PORT=('127.0.0.1',9999)
    sk=socket.socket()

    sk.connect(IP_PORT)
 
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))

   

    while True:
        inp=raw_input('>>>')
        path=inp

        path=os.path.join(BASE_DIR,path)
        print path

        filename=os.path.basename(path)
        print filename

        file_size=os.stat(path).st_size
        print file_size


        file_info='post|%s|%s'%(filename,file_size)

        sk.sendall(bytes(file_info))
        has_sent=0



        with open(path,'rb') as fp:
            while has_sent!=file_size:

                data=fp.read(1024)
                sk.sendall(data)


                has_sent+=len(data)
                #print('\r'+'[progress]:%s.02f%%'%('>'*int((has_sent/file_size)*50),float(has_sent/file_size)*100),end='')
        print()
        print("%s upload ok"%filename)
if __name__=="__main__":
    client()