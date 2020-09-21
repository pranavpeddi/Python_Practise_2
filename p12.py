
class Person:

    name=""
    age=0
    sex=""

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def __GetData__(self):
        print(self.name+str(self.age)+self.sex)



p=Person("pranav",50,"male")
p.__GetData__()



