# -*- coding: UTF-8 -*-

import threading
import time

class MyThreadLock(threading.Thread):  #继承threading.Thread类
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self) #调用父类构造方法
		self.threadID = threadID
		self.name = name;
		self.counter = counter
	
	def run(self):
		print 'Starting:'+ self.name
		threadLock.acquire()
		print_time(self.name,self.counter,5)
		threadLock.release()
		print 'Exiting '+ self.name

def print_time(threadName,delay,counter):
	while counter:
		time.sleep(delay)
		print '%s: %s' %(threadName,time.ctime(time.time()))
		counter -= 1

threadLock = threading.Lock()
threads = []

thread1 = MyThreadLock(1, "Thread-1", 1)
thread2 = MyThreadLock(2, "Thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
	t.join()

print 'Exit Main Thread'