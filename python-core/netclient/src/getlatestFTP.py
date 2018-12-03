import ftplib
import os
import socket

HOST='ftp.mozilla.org'
DIRN='pub/mozilla.org/webtools'
FILE='bugzilla-LATEST.tar.gz'
#PROXY_INFO = { 'host' : 'proxy.piccnet.com.cn',
#               'port' : 3128,
#               }
def main():
    # 连接FTP
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror) as e:
        print('ERROR: cannot reach "%s"' % HOST)
        return
    print('***Connected to host "%s" ' % HOST)
    # 登录
    f.login()
    print('*** Logged in as "annonymous"')

    # 切换路径
    f.cwd(DIRN)
    print('*** Changed to %s folder' % DIRN)

    # 读取二进制文件
    f.retrbinary('PETR %s' % FILE,open(FILE,'wb').write())

    f.quit()

if __name__ == '__main__':
    main()