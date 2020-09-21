import mysql.connector

myconn=mysql.connector.connect(host="localhost",user='root',password="msdhoni07",database="pydb")

cursor=myconn.cursor()

try:
    cursor.execute("select * from remo")
    result=cursor.fetchone()


#reading all rows of the table

   # for x in result:
    #    print(x)

    print(result)




except:
    myconn.rollback()