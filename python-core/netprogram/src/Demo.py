from socket import *

#Python支持的套接字类型AF_INET（基于网络）、AF_NETLINK（Linux套接字）、AF_TIPC（透明进程间通讯，集群使用）、AF_UNIX（进程间）
# 每种套接字类型支持两种风格的套接字连接，SOCK_STREAM（面向连接，TCP）、SOCK_DGRAM（面向无连接，UDP）
# 面向链接的套接字
tcpSocket =socket(AF_INET,SOCK_STREAM)

