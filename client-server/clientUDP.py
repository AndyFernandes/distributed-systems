import socket

# ip = '192.168.56.1'
# port = 7000
ip = input("Digite o IP do servidor: ")
port = input("Digite a porta: ")
addr = ((ip, port))

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Digite o comando desejado: UPTIME\nREQNUM\nCLOSE')
    udp.sendto(msg.encode(), (ip, port))
    print('Mensagem enviada!\n')
    if(msg == 'CLOSE'):
        print('Encerrando conexao...')
        break
udp.close()