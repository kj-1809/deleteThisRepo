# create a binary file namely myfile.info and write a string having two lines in it

import pickle
string = "This is my first line , This is second line"
with open("myfile.info" , "wb") as fh:
  pickle.dump(string , fh)

