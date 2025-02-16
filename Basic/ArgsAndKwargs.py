# *args and **kwargs are list of arguments
# They allow the use of variable amount of arguments in a function

# *args is a list that can be iterated:

name1 = 'Joel'
name2 = 'Robson'
name3 = 'Luigi'

def printnames(*names):
    for name in names:
        print(f"The name is: {name}")

printnames(name1, name2, name3) # try adding a new arg and see what happens
# The name is: Joel
# The name is: Robson
# The name is: Luigi

# **kwargs on the other hand stands for key word arguments
# This means **kwargs is a dictionary with pairs key : value
# Dictionary must be iterated with a method like .items(), .keys() or .values()

def printkwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize():<10}| is |{value:>10}")
    
printkwargs(name='Hector', age=20, grade=7.5) # try changing the args and see what happens
# Name      | is |    Hector
# Age       | is |        20
# Grade     | is |       7.5