#notes on reading files
#need to create a sample.txt file
with open("sample.txt", "r") as file:
   # print(file.read()) #this will print out the entire contents of that file
   # print(file.read(21)) #this will print out "sample test file for "
   data = file.readlines()
   
   for x in data:
      print(x) # list items from using file.readlines will print 1 line at a time