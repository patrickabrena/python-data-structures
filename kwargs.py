#example of using args so that a function can accept n amount of args

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4,5,6,4,5,6))


#example of kwargs
#say you want to calculate the total bill of a restaurant

def kwarg_sum_of(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += value
    return round(sum, 2)

print("$" + str(kwarg_sum_of(coffee=2.99, cake=4.55, juice=2.99)))

