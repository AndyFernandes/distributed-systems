import socket
import os
import sys
from datetime import datetime

start = datetime.now()
contRequests = 0
openSocket = True
host = socket.gethostbyname(socket.gethostname())
port = input("Port: ")
addr = (host, int(port))

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)

while True:
    print('Waiting connection...')
    openSocket = True
    con, cliente = serv_socket.accept()
    contRequests += 1
    print("\nConnected with ", cliente)
    
    while openSocket:
        msg = con.recv(1024)
        print("\nMessage: ", msg.decode())
        
        if(msg.decode() == 'UPTIME'):
            con.send(("Current Time = " + str(datetime.now() - start)).encode())
        elif(msg.decode() == 'REQNUM'):
            con.send(("Connectios = " + str(contRequests)).encode())
        elif(msg.decode() == 'CLOSE'):
            print('Finishing connection...\n')
            openSocket = False
            break
serv_socket.close()


