import mysql.connector

mycon = mysql.connector.connect(host = "localhost", user = "mike", passwd = "yourPass" , database = "test")

if mycon.is_connected() == False:
  print("Error connecting to MySQL database")

cursor = mycon.cursor()
cursor.execute("select * from student")
data = cursor.fetchmany(4)
count = cursor.rowcount

for row in data:
  print(row)


print("Total rows : " , count)
mycon.close()
