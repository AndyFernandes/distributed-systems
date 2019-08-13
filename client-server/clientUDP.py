import socket

ip = socket.gethostbyname(socket.gethostname())
port = input("Port: ")
addr = ((ip, int(port)))

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = raw_input('\n\nWhat are you want?\nUPTIME: Time the server is active\nREQNUM: Number of requests\nCLOSE: Finish connection\n: ')
    udp.sendto(msg.encode(), addr)
    print('\nMessage sent!')
    if(msg == 'CLOSE'):
        print('Finishing connection...')
        break

    newMsg, server = udp.recvfrom(1024)
    print("RESPONSE: \n")
    print(newMsg.decode())

udp.close()