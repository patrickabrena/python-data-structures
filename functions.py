#going to include a function to calculate tax
#
#Function Syntax
#def <function name>(<params>):
#    <taks to complete>

#CALCULATE TOTAL WITH TAX FUNCTION
#bill = 175.00
#
#tax_rate = 15
#
#total_tax = (bill * tax_rate) / 100
#
#print("total tax = ${}".format(total_tax))

#the code chunk above is not a reuseable piece of code

# the function below will be

def calculate_tax(bill, tax_rate): # bill and tax_rate are the parameters as they are place holder values
    return round((bill * tax_rate) / 100, 2)
#the values we pass through the functions are the arguments
print(calculate_tax(175.4568, 15))
