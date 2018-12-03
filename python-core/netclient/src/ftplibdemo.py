import logging
from ftplib import FTP

class MyFtp():
    def __init__(self):
        self.ftp_client = FTP()

    def ftp_login(self,host_id,username,password):
        try:
            self.ftp_client.connect(host_id,port=22,timeout=10)
        except:
            logging.warning('network connect time out')
            return 1001
        try:
            self.ftp_client.login(user=username,passwd=password)
        except:
            logging.warning('username or password error')
            return 1002
        return 1000

    def execute_command(self):
        command_result = self.ftp_client.sendcmd('pwd')
        logging.warning('command_result:%s'% command_result)
        command_result = self.ftp_client.pwd()
        logging.warning('command_result:%s' % command_result)
        # 上传文件 STOR为FTP上传命令
        command_result = self.ftp_client.storbinary('stor ftp_client.py',open("ftp_client.py",'rb'))
        logging.warning('command_result:%s' % command_result)
        # 下载文件 RETR为FTP下载命令
        command_result = self.ftp_client.retrbinary('retr .bash_profile', open('local_bash_profile', 'wb').write)
        logging.warning('command_result:%s' % command_result)

    def ftp_logout(self):
        logging.warning('now will disconnect with server')
        self.ftp_client.close()

if __name__ == '__main__':
    # 要连接的主机ip
    host_ip = '192.68.220.128'
    # 用户名
    username = 'ls'
    # 密码
    password = 'abcd1234'
    # 实例化
    my_ftp = MyFtp()
    # 如果登录成功则执行命令，然后退出
    if my_ftp.ftp_login(host_ip,username,password) == 1000:
        logging.warning('login success , now will execute some command')
        my_ftp.execute_some_command()
        my_ftp.ftp_logout()