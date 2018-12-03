import  _thread
from time import sleep,ctime

def loop0():
    print('start loop 0 at:',ctime())
    sleep(4)
    print('loop 0 done at:',ctime())

def loop1():
    print('start loop 1 at:',ctime())
    sleep(2)
    print('loop 1 done at:',ctime())

def main():
    print('starting at:'+ctime())
    _thread.start_new_thread(loop0,())
    _thread.start_new_thread(loop1,())
    # 主线程必须增加sleep，否则直接退出，子线程不会被强制终止
    sleep(6)
    print('all DONE at:'+ctime())

if __name__ == '__main__':
    main()