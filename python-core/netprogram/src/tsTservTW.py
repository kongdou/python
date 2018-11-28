from twisted.internet import protocol,reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    # 客户端连接到服务器时执行
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from :',clnt)
    # 服务器接收到网络发送的数据时调用
    def dataReceived(self, data):
        self.transport.write(('[%s ] %s' % (ctime(),data.decode())).encode())

# 协议工厂
factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
# 监听
reactor.listenTCP(PORT,factory)

# 运行
reactor.run()
