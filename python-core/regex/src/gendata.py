from random import randrange,choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds=('com','edu','net','org','gov')
for i in range(randrange(5,11)):
    dtint = randrange(maxsize)
    dtstr = ctime()
    llen = randrange(4,8) # 长度随机值4-8
    login = ''.join(choice(lc) for j in range(llen)) # 生成4-8位用户名
    dlen = randrange(llen,13) # 长度
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr,login,dom,choice(tlds),dtint,llen,dlen))
