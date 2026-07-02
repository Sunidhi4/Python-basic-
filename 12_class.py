# # #  class : class is a blueprint to creating an object.
# # class Employee:
# #     language = "Py"  #this is an class attribute 
# #     salary = 120000

# #     def __init__(self, name, salary, language):   #dunder method which is automatically call.
# #         self.name = name
# #         self.salary = salary
# #         self.language = language
# #         print("I am creating an object")

# #     def getInfo(self):
# #         print(f"the language is {self.language}. The salry is {self.salary}")

# #     def greeting(self):
# #         print("Good morning")

# # harry = Employee("Haary", 1300000, "javascript")
# # print(harry.name, harry.language)
# # # harry.language = "javascript"  #this is an insatnce attribute
# # harry.getInfo()
# # harry.greeting()

# #practice set
# # 1.
# # class Programmer:
# #     company = "Microsoft"
# #     def __init__(self, name, salary, pin):
# #         self.name = name
# #         self.salary = salary
# #         self.pin = pin

# # p = Programmer("Sunidhi", 1200000, 243533)
# # print(p.name, p.salary, p.pin, p.company)
# #  2.
# class Calculator:
#     def __init__(self, n):
#         self.n = n
    
#     def square(self):
#         print(f"the square is {self.n*self.n}")
    
#     def cube(self):
#         print(f"the cube is {self.n*self.n*self.n}")

#     def squareroot(self):
#         print(f"the square root is {self.n**1/2}")

#     @staticmethod
#     def Hello():
#         print("Hello there!")  #static method 

# a = Calculator(4)
# a.square()
# a.cube()
# a.squareroot()
# a.Hello()

# # 3.
# from random import randint
# class Train:
    
#     def __init__(self, trainNo):
#       self.trainNo = trainNo

#     def book(self, fro, to):
#         print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")

#     def getStatus(self):
#         print(f"train no : {self.trainNo} is on time")

#     def getFare(self, fro, to):
#         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 555)}")

# t = Train(12322)
# t.book("Rampur", "Delhi")
# t.getStatus()
# t.getFare("Rampur", "Delhi")
