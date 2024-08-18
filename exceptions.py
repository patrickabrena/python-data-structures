#notes on handling exceptions with try and except statements
def divide_by(a, b):
    return a / b

try:
    ans = print(divide_by(40, 0))

except ZeroDivisionError as e:
    print(e, "cant divide by zero")

except Exception as e:
    #can isolate the exceotion using Exception as e: and then include e in print statement to see what type of exception it is
    # Exception is generic but you can also do except ZeroDvisionError as e if you know what exception you're looking for
    print("Something went wrong", e)
    #can also print the class of the exception as well
    print(e.__class__) #will print <class 'ZeroDivisionError'>


#print(divide_by(40, 0)) this will throw ZeroDivisionError