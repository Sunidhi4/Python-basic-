# class Employee:
#     company = "ITC"
#     name = "Default name"
#     def show(self):
#         print(f"the name of the employee is {self.name} and the company is {self.company}")

# class Coder:
#     language = "python"
#     def printLanguage(self):
#         print(f"All of the above languages yout language is : {self.language}")

# class Programmer(Employee, Coder):  #multiple inheritance
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The company is {self.company} and he is good with {self.language} language")

# a = Employee()
# b = Programmer()

# print(a.company, b.company)
# b.show()
# b.showLanguage()
# b.printLanguage()

# Multilevel inheritance
# class Employee:
#     a = 1

# class Programmer(Employee):
#     b = 2

# class Manager(Programmer):
#     c = 3

# o = Employee()
# print(o.a)  # print the a attribute
# # print(o.b) #show an error . There is no b attribute in Employee class

# o = Programmer()
# print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)

# Super 
# class Employee:
#     def __init__(self):
#         print("Constructor of Employee")

# class Programmer(Employee):
#     def __init__(self):
#         print("Constructor of Programmer")

# class Manager(Programmer):
#     def __init__(self):
#         super().__init__()  # It will call super class constructor also
#         print("Constructor of Manager")

# o = Employee()
# o = Programmer()
# o = Manager()

# Class Method : A class method is a method which is bound to the class and not the object of the class.
#  @classmethod decorator is used to create a class method.

# class Abb:
#   a = 10
#   @classmethod
#   def show(cls):
#    print(f"the class method attribute is {cls.a}")

# a = Abb()
# a.a = 23
# a.show()

# Property decorator
# class Employee:
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
    
#     @name.setter
#     def name(self, value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# e = Employee()
# e.name = "Sunidhi Soner"
# print(f"first name : {e.fname} , last name : {e.lname}" )

# Operator overloading
# Operators in pyhton can be overloaded using dunder methods. These methods are called when a given operator is used on the objects. 

class Number:
    
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
n = Number(1)
m = Number(2)

print(n + m)