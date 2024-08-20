#Practicing traping exceptions
# Starter code
items = [1,2,3,4,5]
#item = items[6] index error should be inside the "try" block because this si wher the indexError might occur
try:
    item = items[6]
    print(item)

except IndexError as e: 
    print(e, "Item does not exit")


# Starter code
def divide_by(a, b):
    try:
        return a / b # wrapping the return a/b within try because if is possible it will perform a/b when called with the divide_by function
    except ZeroDivisionError:
        return 0 # wrapping the return 0 in the except ZeroDivisionError statement will return zero when the error is thrown after trying 40/
    0

ans = divide_by(40, 0)
print(ans)


# Starter code
#wrap this whole "with" statement in a try
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("FIle not foud. Returning an empty string")