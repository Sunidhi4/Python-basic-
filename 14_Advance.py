# # Walrus operator : the walrus operator (:=), introduced in Python 3.8, allows you to assign values to variables as 
# # part of an expression. This operetor, named for its resemblance tothe eyes and tasks of a walrus, is officially
# #  called the assignment expression.

# if(n := len([1, 2, 3, 4, 5])) > 3:
#     print(f"List is too long ({n} elements, expected <= 3)") 

# # Types Definition in Python : Type hints are added using the colon (:) syntax for variables and the -> syntax for
# # function return types.
# n : int  = 5
# name : str = "Harry"

# def sum(a : int, b : int) -> int:
#     return a+b

# # Advanced type hints : Python's typing module provides more advanced type hints, such as List, Tuple, Dict, and 
# # Union. You can import List, Tuple, and Dict types from the typing module.these annotation help in making the code 
# # self-documenting and allow developers to understand the data structure used at a glance.


# # Match Case : Python 3.10 introduced the match statement, which is similar tothe switch statement found in other 
# # programming languages. The basic syntax of the match statement involves matching a variable against several 
# # cases using the case keyword.

# def http_status(status):
#     match status:
#         case 200 : 
#             return "OK"
#         case 404 : 
#             return "Not Found"
#         case 500 :
#             return "Internal Server Error"
#         case _ :
#             return "Unknown status"

# print(http_status(500))

# # Dictionary Merge and Update Operators : 
# dict1 = {'c' : 1, 'd' : 2}
# dict2 = {'e': 4, 'f' : 5}
# merged = dict1 | dict2
# print(merged)

# # you can now use multiple conatct manager in single with statement more clearly using the parenthesised content
# # manager

# # with (
# #     open("file.txt") as f1,
# #     open("hiscore.txt") as f2
# # ):
#     #   process files

# # Exceptional Handling: Exception in python can be handled using a try statement. The code that handles the 
# # exception in written in the clauses.

# # try:
# #     a = int(input("hey , Enter a number :"))
# #     print(a)

# # except Exception as e :
# #     print(e)

# # print("Thank you")

# # Raising Exceptions : we can raise custom exception using the 'raise' keyword in python.

# # a = int(input("Enter a number : "))
# # b = int(input("Enter second nnumber: "))

# # if(b == 0):
# #     raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
# # else :
# #     print(f"the division a/b is {a/b}")

# # try with else: Sometimes we want to run a piece of code when try was successful.

# # try:
# #     a = int(input("hey , Enter a number :"))
# #     print(a)

# # except Exception as e :
# #     print(e)

# # else:
# #    print("I am inside the else ")

# # Try with Finally:
# # Python offers a 'finally' clause which ensure execution of a piece of code inspective of the exception.

# def main():

#      try:
#         a = int(input("hey , Enter a number :"))
#         print(a)
#         return

#      except Exception as e :
#         print(e)
#         return
     
#      finally:
#         print("I am inside the finallyy") 

# main()

# Global keyword: 'global' keyword is used to modify the variable outside of the current scope.

# Enumerate function: the 'enumerate' function adds counter to an iterable and retirns it.

# l = [3,4,23,12]

# for index, item in enumerate(l):
#     print(f"the item number at index {index} is {item}")

# List Comprehensions : List comprehennsions is an elegant way to create lists based on existing lists.

myList = [1, 2, 3, 4, 5, 6]

squaredList = [i*i for i in myList]

print(squaredList)

