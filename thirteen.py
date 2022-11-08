import mysql.connector

mycon = mysql.connector.connect(host = "localhost", user = "mike", passwd = "yourPass" , database = "test")

if mycon.is_connected() == False:
  print("Error connecting to MySQL database")

cursor = mycon.cursor()
st = "select * from student where marks > %s and section = '%s'" % (90 , 'C')
cursor.execute(st)
data = cursor.fetchall()

for row in data:
  print(row)

mycon.close()
