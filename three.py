# write a program to that checks for the presence of a value inside a dictionary and prints its key 

info = {'Riya' : 'CSc' ,
'Mark Rober' : 'Economics',
'Isha' : 'Eng',
'Steve' : 'Social Science'}

inp = input("Enter value to be searched for : ")
if inp in info.values():
  for a in info:
    if info[a] == inp:
      print("The key of a given value is" , a)
      break 
    else:
      print("Given values does not exist in dictionary")

