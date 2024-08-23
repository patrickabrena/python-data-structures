# Storing file contents in data structures


#imagine you're trying to come up with names for new pet, you're unsure
#so you use python to help you decide

#you start by acessing a file with a shortlist of names

#name the file petnames.txt


#now going to use python to randomly pick one

#to do this, you'll need to have a python file into which you'll be importing petnames.txt file

#importing the random module at the top of the my code
import random

f = open("petnames.txt", "r")

#The open() function reads in a file outside of the program itself

#The open() function accepts two parameters:

#1. The path and the filename in the form of a string
#2. The import mode(the default being "r" - which is "read")

#In the actual line of code above, i'm importing the file at the root of the project.
#so only need to specify the file name without the path
#also using the default "r" mode to read in the file
#saving imported file into a variable named f

#next, going to add another variable, f_content, and assigning it to the result of reading the f file

#this is like the with open() statement except you're storing the opening of petnames.txt in f then using .read nethod to read the lines

f_content = f.read()

#print(f_content)

#Now that it's confirmed that the file is successfully being read, I can comment out print(f_content)

#Additionally, you can get the f_content variable into a list.
#The string "\n" is used to split the text where a new line is found

f_content_list = f_content.split("\n")

#print(f_content_list)

#this is the output from that print statement
#['Ace', 'Atlas', 'Bailey', 'Bear', 'Blaze', 'Boomer', 'Buddy', 'Coco', 'Cooper', 'Duke', 'Dozer', 'Echo', 'Gizmo', 'Harley', 'Mac', 'Max', 'Milo', 'Oscar', 'Rex', 'Rocky', 'Rocket', 'Wolfie']
                                 
#make sure there's an import random module at the top of the code

#Now I can use the random module's choice() function: random.choice()

#The choice() function accepts a sequence paramter. 
#A list is one of its accepted values. 
f.close()
print(random.choice(f_content_list))