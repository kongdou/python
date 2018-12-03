import  _thread
from time import sleep,ctime

loops = [4,2]
def loop(nloop,nsec,lock):
    print('start loop ',nloop,'at :',ctime())
    sleep(nsec)
    lock.release()

def main():
    print('start at:'+ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        # 获得锁对象
        lock = _thread.allocate_lock()
        # 取得锁
        lock.acquire()
        # 增加到锁列表
        locks.append(lock)

    # 同时启动线程，获得锁需要花费时间，不能放到上一个for循环中，否则线程太快，还未分配到锁就执行完成
    for i in nloops:
        _thread.start_new_thread(loop,(i,loops[i],locks[i]))

    # 暂停主线程，等待所有的锁释放后主进程执行完成
    for i in nloops:
        while locks[i].locked() : pass
    print('all DONE at:'+ctime())

if __name__=='__main__':
    main()