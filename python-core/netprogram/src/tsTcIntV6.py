from socket import *

HOST='::1'
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpCliSock = socket(AF_INET6,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZE).decode()
    if not data:
        break
    print(data)
tcpCliSock.close()