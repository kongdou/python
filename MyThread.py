# -*- coding: UTF-8 -*-

import threading
import time

exitFlag = 0


class MyThread(threading.Thread):  #继承threading.Thread类
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self) #调用父类构造方法
		self.threadID = threadID
		self.name = name;
		self.counter = counter
	
	def run(self):
		print 'Starting:'+ self.name
		print_time(self.name,self.counter,5)
		print 'Exiting '+ self.name
		

def print_time(threadName,delay,counter):
	while counter:
		if exitFlag:
			print 'ExitFlag:' + `exitFlag`
			#(threading.Thread).exit()
		time.sleep(delay)
		print '%s: %s' %(threadName,time.ctime(time.time()))
		counter -= 1


thread1 = MyThread(1,"thread-1",1)
thread2 = MyThread(2,"thread-2",2)


thread1.start()
thread2.start()

print 'Exit Main Thread'