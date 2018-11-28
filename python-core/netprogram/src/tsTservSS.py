from socketserver import  (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST=''
PORT=21567
ADDR=(HOST,PORT)

# 定义StreamRequestHandler子类，处理客户端连接
class MyRequestHanlder(SRH):
    def handle(self):
        print('...contected from:',self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(),self.rfile.readline().decode())).encode())

tcpServ=TCP(ADDR,MyRequestHanlder)
print('waiting for connection...')
tcpServ.serve_forever()
