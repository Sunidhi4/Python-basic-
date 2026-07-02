# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return n*fact(n-1)


# print(fact(5))

# practice set 
# 1.
# def greatest(a, b, c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
    
# a = int(input("Enter your number 1 : "))
# b = int (input("Enter your number 2 : "))
# c = int (input("Enter your number 3 : "))

# print(f'The greatest of all number is {greatest(a,b,c)}')

# 2.
# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter temparature in F: "))
# c = f_to_c(f)
# print(f"{round(c,2)} degree celsius")

# 3.
# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)

# pattern(5)

# 4.
# def inch_to_cms(inch):
#     return inch * 2.54

# n = int(input("Enter value in inches: "))

# print(f"The corresponding value in cms is {inch_to_cms(n)}")

# 5.
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["harry", "rohan", "shubham", "an"]

print(rem(l, "an"))