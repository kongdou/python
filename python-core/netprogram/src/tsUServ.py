from socket import *
from time import ctime

HOST=""
PORT=21567
BUFFSIZE=1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    data,address = udpSerSock.recvfrom(BUFFSIZE)
    print('接收数据:'+data.decode())
    udpSerSock.sendto(('[%s] %s' % (ctime(),data)).encode(),address)
    print('...received from and return to:',address)
    if (data.decode() == 'bye'): # 从客户端接收到bye，关闭连接
        udpSerSock.close()

