# -*- coding: UTF-8 -*-
import Code

class Parent:
	'父类'
	def __init__(self):
		print Code.coder('父类构造方法')
	
	def parentMethod(self):
		print Code.coder('调用父类方法')
	
	def setAttr(self,attr):
		Parent.parentAttr = attr
	
	def getAttr(self):
		print Code.coder('父类属性：'),Parent.parentAttr
		

class Child(Parent):
  '子类'
  def __init__(self):
  	print Code.coder('调用子类构造方法')
  
  def childMethod(self):
  	print Code.coder('调用子类方法')
  	

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
  