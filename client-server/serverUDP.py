import socket
from datetime import datetime

start = datetime.now()
contRequests = 0

host = input("Digite o IP do servidor: ")
port = input("Digite a porta: ")
addr = (host, port)

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(addr)

while True:
    msg, cliente = udp.recvfrom(1024)
    contRequests += 1
    # print(cliente)
    print(msg.decode())
    if(msg.decode() == 'UPTIME'):
        print("Current Time = ", (datetime.now() - start).strftime("%H:%M:%S"))
    elif(msg.decode() == 'REQNUM'):
        print("Connectios = ", contRequests)
    elif(msg.decode() == 'CLOSE'):
        print('Finishing connection...')
        break
udp.close()
