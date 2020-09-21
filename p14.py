class Person:

    name=""
    gender=""

    def __init__(self,n,g):
        self.name=n
        self.gender=g

    def getName(self):
        print(self.name)

    def getGender(self):
        print(self.gender)




class Employee(Person):
        
    def __init__(self):
        self.salary=25000

    def getSalart(self):
        print("employee name",Person.name,"and salary is",self.salary)


    def Main(self):
        e=Person("pranav","male")
        e=Employee()
        e.getSalart()

    if __name__ == '__main__':
        Main()