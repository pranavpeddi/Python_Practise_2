# how to access variables of super class

class Base(object):

    def __init__(self,x):
        self.x=x

class Derived(Base):


    def __init__(self,x,y):
        Base.x=x
        self.y=y

    def printXY(self):

        print(Base.x,self.y)

d=Derived(10,5060)
d.printXY()
