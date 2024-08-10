#notes on python dictionaries
#dictionaries look up values based on keys, NOT by index so it makes them faster

#python uses key value pair in dictionary
#values are mutable in key value pairs in a dictionary

#python dictionary syntax
sample_dict = {1: "Coffee", 2: "Tea", 3: "Juice",}
print(sample_dict[1])

#you can iterate with a dictionary as well 
#you need to print out both key and value try this
for key, value in sample_dict.items():
    print("{} : {}".format(str(key), value))