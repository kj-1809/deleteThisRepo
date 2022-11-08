# Write a program to create a CSV file to store student data (Roll no. , Name , Marks)
# Obtain data from user and write 5 records into the file

import csv
fh = open("Students.csv", "w")
stuwriter = csv.writer(fh)
stuwriter.writerow(['Rollno' , 'Name' , 'Marks'])

for i in range(5):
  print("Student record" , (i+1))
  rollno = int(input("Enter roll no. : "))
  name = input("Enter your name : ")
  marks = float(input("Enter marks : "))
  sturec = [rollno , name , marks]
  stuwriter.writerow(sturec)

fh.close()

