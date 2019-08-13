import socket

ip = socket.gethostbyname(socket.gethostname())
port = input("Port: ")
addr = ((ip, int(port)))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

while True:
    msg = raw_input('\nWhat are you want?\nUPTIME: Time the server is active\nREQNUM: Number of requests\nCLOSE: Finish connection\n: ')
    client_socket.send(msg.encode())
    print('\nMessage sent!')
    if(msg == 'CLOSE'):
        print('Finishing connection...')
        break
    print("\nRESPONSE: \n")
    newMsg = client_socket.recv(1024)
    print(newMsg)
client_socket.close()

