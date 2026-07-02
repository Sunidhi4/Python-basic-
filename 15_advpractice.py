#  1.
# try:
#     with open("file0.txt", "r") as f1: print(f1.read())
# except Exception as e :
#     print(e)
# try:
#     with open("file1.txt", "r") as f2: print(f2.read())
# except Exception as e :
#     print(e)
# try:
#     with open("file2.txt", "r") as f3: print(f3.read())
# except Exception as e :
#     print(e)

# 2.
# l = [1, 2, 3, 4, 5, 6, 7]

# for i, item in enumerate(l):
#     if i == 2 or i == 4 or i == 6:
#         print(item)

# 3.
# n = int(input("enter your number: "))

# table = [n*i for i in range(1,11)]

# print(table)

# 4.
try:
    a = int(input("enter a : "))
    b = int(input("Enter b : "))
    print(a/b)
except ZeroDivisionError as e :
    print("infinite")