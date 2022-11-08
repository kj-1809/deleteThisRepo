#displaying the size of a file after removing EOL character,  leading and trailing white spaces and blank lines 

myfile = open("data.txt" , "r")
str1 = " "
size = 0
tsize = 0
while str1:
  str1 = myfile.readline()
  tsize = tsize + len(str1)
  size = size + len(str1.strip())

print("Size of the file after removing all EOL characters & blank lines : ", sizes)
print("The total size of the file : " , tsize)  
myfile.close()

