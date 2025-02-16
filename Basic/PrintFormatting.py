# This file will explain formatting in python function : print
# There are many ways to print but the fastest is f-string
# Here's a demo

name = 'Jonh'
print(f"The name is {name}")

# For alignment it is used as {num1:>5}
num1 = 1
print(f"{num1:>5}") # '    1'
print(f"{num1:<5}") # '1    '
print(f"{num1:^5}") # '  1  '

#formatting with something other than space is possible:
print(f"{num1:.>5}") # '....1'
print(f"{num1:->5}") # '----1'
print(f"{num1:/>5}") # '////1'


# Formatting has cool uses, here's one
names = ('John', 'Mathew', 'Tobias', 'Maria')

index = 1
for name in names:
    print(f"The |{index:>3}º| name is |{name:>10}|")
    index += 1
# Expected:
# The |  1º| name is |      John|
# The |  2º| name is |    Mathew|
# The |  3º| name is |    Tobias|
# The |  4º| name is |     Maria|