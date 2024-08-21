#notes on file handling in python
#first we need to create a test file
file = open("file.txt", mode = "r")

data = file.readline()

print(data)

file.close()

#can also do this in another way
#creating a new file to demonstrate "with open" method which auto closes the file for me
with open("test.txt", mode = "r") as file:
    data1 = file.readline()
    print(data1)