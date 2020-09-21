import  mysql.connector

myconn=mysql.connector.connect(host="localhost",user='root',password="msdhoni07",database="pydb")

#print(myconn)

cur=myconn.cursor()

sql="insert into remo(name,occupation) values (%s, %s)"

sql2="create table remo(name varchar(40), occupation varchar(20))"
val = ("Pranav","Male")
sql3="select * from remo"

try:
   # cur.execute(sql,val)
#   cur.execute(sql,val)
 #  myconn.commit()

    cur.execute(sql3)
    result=cur.fetchall()

    for x in result:
          print(x)

   print("data is inserted")


except:
    print("there is an exception")
   # print(error.message)
    myconn.rollback()



#print("data inserted")
myconn.close()