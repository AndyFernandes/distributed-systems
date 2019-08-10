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

# Instancia o SOCKET
# 1o PARAMETRO: socket.AF_INET: Familia do protocolo
# 2o PARAMETRO: socket.SOCK_STREAM: Inidica que é TCP/IP
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# zerar o TIME_WAIT do Socket, por exemplo, se o programa estiver aguardando uma conexão e você der CTRL+C para interromper, o programa  será fechado, porém o Socket continua na escuta
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# qual IP e porta o servidor deve aguardar a conexão
serv_socket.bind(addr)
# Limite de conexões
serv_socket.listen(10)

while True:
    print('Waiting connection...')
    openSocket = True
    con, cliente = serv_socket.accept()
    contRequests += 1
    print("\nConnected with ", cliente)
    
    while openSocket:
        # Aguarda um dado enviado pela rede de até 1024 Bytes - Tamanho do Buffer de recepção
        msg = con.recv(1024)
        print("\nMessage: ", msg.decode())
        
        if(msg.decode() == 'UPTIME'):
            print("Current Time = ", (datetime.now() - start))
        elif(msg.decode() == 'REQNUM'):
            print("Connectios = ", contRequests)
        elif(msg.decode() == 'CLOSE'):
            print('Finishing connection...\n')
            openSocket = False
            break
serv_socket.close()


