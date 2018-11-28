from socket  import *
from time import ctime

# Socket服务端
HOST=''
PORT=21567
BUFSIZE=1024
ADDR = (HOST,PORT)

tcpSerSocket = socket(AF_INET,SOCK_STREAM)
tcpSerSocket.bind(ADDR)
tcpSerSocket.listen(5) # 连接被转接或拒绝前，传入请求的最大数

while True:
    print("waiting for connection...")
    tcpCliSocket,addr = tcpSerSocket.accept()
    print("connected from:",addr)

    while True:
        data = tcpCliSocket.recv(BUFSIZE).decode()
        print("接收数据:"+data)
        if not data:
            break
        tcpCliSocket.send(('[%s] %s' % (ctime(),data)).encode())
    tcpCliSocket.close()
tcpCliSocket.close()