import socket
from datetime import datetime

start = datetime.now()
contRequests = 0

host = input("Digite o IP do servidor: ")
port = input("Digite a porta: ")
addr = (host, port)

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

print('Aguardando conexao\n')
while True:
    con, cliente = serv_socket.accept()
    # Aguarda um dado enviado pela rede de até 1024 Bytes - Tamanho do Buffer de recepção
    msg = con.recv(1024)
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
serv_socket.close()


