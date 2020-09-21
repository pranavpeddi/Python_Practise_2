class Person(object):

    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(Person):

    def isEmployee(self):
        return True

emp = Person("Pranav")
emp2=Employee("Pranav")
print(emp.getName(),emp.isEmployee())
print(emp2.getName(),emp.isEmployee())