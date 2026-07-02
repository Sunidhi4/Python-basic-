from functools import reduce
# Virtual Environment : An environment which is same as the system interpreter but is isolated from the other 
# Python environment


# pip freeze : 'pip freeze' returns all packages installed ina given environment along with the versions.
# pip freeze > requirements.txt
# the above command creates a file named 'requirements.txt' in the same directory containing the output of 'pip freeze'
# we can distribute this file to other users, and they can recreate the same snvironment using :
# pip install -r requirements.txt

# Lambda Function : Function created using an expression using 'lambda' keyword.

# square = lambda x: x*x
# print(square(4))

# Join method (strings): Create a string from iterable objects.

# l = ["sunidhi", "shreya", "lia"]

# final = "::".join(l)
# print(final)  # ans = sunidhi::shreya::lia

# Map example:

l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)

print(list(sqList))

# Filter example:
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce example:
def sum(a, b):
    return a + b 

print(reduce(sum, l))
