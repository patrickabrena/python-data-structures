# different types of scope in python

#local scope, enclosing scope, global scope, built in

#variables within the built-in and global scope are accessible from anywhere in the code

#global scope example
my_global = 10

def fn1():
    enclosed_v = 8
    def fn2():

        local_v = 5
        print("Acces to Global", my_global)
        print("Access to enclosed", enclosed_v)
    fn2()

fn1()

#print("Can't access local", local_v) #will get error because this print statement is outisde of fn1()

#built in scope are the functions that are reserved keywords like print and def and round