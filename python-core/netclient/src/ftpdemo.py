import ftplib


f = ftplib.FTP('ftp.python.org')
f.login('anonymous','guido@python.org')
f.dir()
