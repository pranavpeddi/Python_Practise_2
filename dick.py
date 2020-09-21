

d={}

for _ in range(int(input())):
   name=input()
   score=float(input())
   d[name]=score


print(d)

v=d.values()

second_lowest=sorted(list(set(v)))[1]

second_list=[]

for key,value in d.items():
     if value==second_lowest:
         second_list.append(key)
second_list.sort()

print([i for i in second_list])


