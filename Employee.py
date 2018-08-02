# -*- coding: UTF-8 -*-

class Employee:
	'‘±π§¿‡'
	empCount = 0
	
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
	
	def displayCount(self):
		print "Total employee %d" % Employee.empCount
	
	def displayEmployee(self):
		print "Name: ",self.name, ", salary: ",self.salary
		

emp1 = Employee("Zara",2000)
emp2 = Employee("Jenkin",5000)

setattr(emp1,"salary","3000")

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" %Employee.empCount
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__