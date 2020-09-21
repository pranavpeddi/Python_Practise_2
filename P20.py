from collections import  Counter

# list1=map(int,input().split())

from collections import OrderedDict

print("this is a dict:\n")

d={}

d['a']=1
d['b']=2
d['c']=3

for key,value in d.items():
    print(key,value)



od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4

print('this is an ordered dictionary')
for key,value in od.items():
    print(key,value)