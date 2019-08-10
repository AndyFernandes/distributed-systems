import socket

# ip = '192.168.56.1'
# port = 7000
ip = input("Digite o IP do servidor: ")
port = input("Digite a porta: ")
addr = ((ip, port))

# Instancia o SOCKET
# 1o PARAMETRO: socket.AF_INET: Familia do protocolo
# 2o PARAMETRO: socket.SOCK_STREAM: Inidica que é TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

while True:
    msg = input('Digite o comando desejado:\nUPTIME\nREQNUM\nCLOSE\n')
    client_socket.send(msg.encode())
    print('Mensagem enviada!\n')
    if(msg == 'CLOSE'):
        print('Encerrando conexao...')
        break
client_socket.close()

