import socket

ip = socket.gethostbyname(socket.gethostname())
port = input("Port: ")
addr = ((ip, int(port)))

# Instancia o SOCKET
# 1o PARAMETRO: socket.AF_INET: Familia do protocolo
# 2o PARAMETRO: socket.SOCK_STREAM: Inidica que é TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

while True:
    msg = input('\nWhat are you want?\nUPTIME: Time the server is active\nREQNUM: Number of requests\nCLOSE: Finish connection\n: ')
    client_socket.send(msg.encode())
    print('\nMessage sent!')
    if(msg == 'CLOSE'):
        print('Finishing connection...')
        break
client_socket.close()

