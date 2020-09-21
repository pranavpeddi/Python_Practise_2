import  collections

dic1={'a':1,'b':2}
dic2={'c':3,'d':4}

chain=collections.ChainMap(dic1,dic2)

print("All the chain Map contents are ")
print(chain.maps)

print(list(chain.values()))
print(list(chain.keys()))