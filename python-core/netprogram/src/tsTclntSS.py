from socket import *

HOST='localhost'
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

while True:
    #SockerServer 请求处理程序的默认行为是接受连接、获取请求，然后关闭连接，所以需要每次发送的时候新建连接
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('>')
    if not data:
        break
    tcpCliSock.send(('%s\n' % data).encode())
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print(data.decode())
    tcpCliSock.close()