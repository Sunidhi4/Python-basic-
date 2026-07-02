# age = int(input("enter your age : "))

# # if elif else ladder

# if(age>=18):
#     print("You are above the age of concent ")
#     print(" good for you")

# elif(age<0):
#     print("you are entering an invalid age")

# elif(age==0):
#     print("You are entering a zero which is not a valid age")

# else:
#     print("You are below the age of concent ")

# print("End of program")

# practice set 
# 1.
# a1 = int(input("enter number 1 : "))
# a2 = int(input("enter number 2 : "))
# a3 = int(input("enter number 3 : "))
# a4 = int(input("enter number 4 : "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number is a1 : ", a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#     print("greatest number is a2 : ", a2)

# elif(a3>a2 and a3>a1 and a3>a4):
#     print("Greatest number is a3 : ", a3)

# else:
#     print("greatest number is a4 : ", a4)

# 2.
# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("enter your comment: ")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("this comment is a spam")

# else:
#     print("this comment is not a spam")

# 3.
l = ["harry", "rohan", "iyush", "div"]

name = input("ENter your name: ")

if(name in l):
    print("Your name is in the list")
else:
    print("your name is not in the list")