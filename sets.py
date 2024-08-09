#notes on sets
#sets don't allow for duplicate values
set_a = {1, 2, 3, 4, 5}


#you can use the add method to add a number to the end of the set
set_a.add(6)


#you can also use the remove or discard method
set_a.remove(5)
set_a.discard(2)


print(set_a)



#you can use union method or the | to append one set to another and it will remove duplicates
set_b = {4, 5, 6, 7, 8, 9}

print(set_a.union(set_b))
print(set_a | set_b)
#both print statements above do the same thing


#you can use intersection method to see which values overlap
print(set_a.intersection(set_b))

#you can use the difference method to see the values in one set but not the other
print(set_a.difference(set_b))
print(set_a - set_b)


#you can use the symmetric operator to show elements in both set_a and set_b but NOT both sets
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)

#AGAIN SETS ARE UNORDERED SO CAN'T ACCESS AN ELEMENT THORUGH REGULAR INDEX WAY