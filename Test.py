class Person:

    def __init__(self,name):
        self.name=name

    def say_hi(self):
        print('hello, my name is',self.name)

    def setAdd(self,address):
     self.address=address

    def getAddress(self):
      return self.address

p=Person('naagu')
p.say_hi();
p.setAdd("warangal")
p.getAddress()