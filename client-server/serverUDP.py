import socket
from datetime import datetime

start = datetime.now()
contRequests = 0
openSocket = True
host = socket.gethostbyname(socket.gethostname())
port = input("Port: ")
addr = (host, int(port))

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(addr)

print('\nWaiting connection...')
while True:
    openSocket = True
    msg, cliente = udp.recvfrom(1024)
    contRequests += 1
    print("\nConnected with ", cliente)
    print("\nMessage: ", msg.decode())

    if(msg.decode() == 'UPTIME'):
        udp.sendto(("Current Time = " + str((datetime.now() - start))).encode(), cliente)
    elif(msg.decode() == 'REQNUM'):
        udp.sendto(("Connectios = " + str(contRequests)).encode(), cliente)
    elif(msg.decode() == 'CLOSE'):
        print('Finishing connection...\n')
        print('\nWaiting connection...')
udp.close()
