import  threading
from time import sleep,ctime

loops = [4,2]

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    print('start loop ',nloop,'at:',ctime())
    sleep(nsec)
    print('loop ',nloop,'done at:',ctime())

def main():
    print('start at:'+ctime())
    threads = []
    nloops = range(len(loops))

    # 增加线程到线程组，但不会立即执行
    for i in nloops:
        t = MyThread(loop,(i,loops[i]),loop.__name__)
        threads.append(t)

    # 启动线程组中的线程
    for i in nloops:
        threads[i].start()

    # 等待线程结束，正常情况可以不用调用，多个线程会一直执行，主线程直接执行该for语句之后的逻辑
    # 除非需要等到线程结束，才允许往后执行
    for i in nloops:
        threads[i].join()

    print('all DONE at:'+ctime())

if __name__=='__main__':
    main()