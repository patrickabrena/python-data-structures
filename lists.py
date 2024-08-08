#list is a dynamic array that can hold any datatype
list1 = [1, 2, 3, 4, 5]

list2 = ["A", "B", "C", "D",]

list3 = ["Hello", 1, True, 30.22]

#print(list3[3])
#this is how to access an item at index 3 of list 3

#print(*list3)
#this prints the entirety of the list

#print(list2, sep = "")
#prints ["A", "B", "C", "D",]



##################

#different ways to modify list

#using insert function
list1.insert(len(list1), 6)
#print(list1, sep = "")

#using append function
list2.append("E")
#print(list2, sep = "")

#using extend function
list3.extend(["A String", False, [1, 2, 3]])
print(list3, sep = "")

#removing items from the list
print(list1.pop(0), sep = "")
print(list1)

del list1[4]
print(list1)

#can also iterate through a list to access the different values through for loop

for x in list2:
    print("Value: ", x)