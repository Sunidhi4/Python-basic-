# # i = 1

# # while(i<6):
# #     print(i)
# #     i += 1

l = [1, "harry", False, "this", "Rohan", "Shubhi"]

# # i=0

# # while(i<len(l)):
# #     print(l[i])
# #     i += 1

# # print("i: ",i)
# # print(".............")

# for j in range(4):
    # print(j)

# print("j: ",j)
# print(".............")

# for k in l:    # for list
    # print(k)

# print("k: ",k)
# print(".............")

# # for tuples
# t = (6, 231, 75, 122)
# for i in t:
    # print(i)

# # for Strings
# s = "Harry"
# for i in s:
    # print(i)

# # for loop with else 
# l = [1, 7, 8]

# for item in l:
#     print(item)

# else:
#     print("done") # this is printed when the loop exhausts!

# for i in range(100):
#     if(i == 34):
#         break #exit the loop
#     print(i)

# for i in range(100):
#     if(i == 34):
#         continue #skip the iteration
#     print(i)

# pass is a null statement in python . it instruct to "do nothing".

# practice set 
# 1.
# n = int(input("Enter your number : "))

# for i in range(n , n*11, n):
    # print(i)

# # 2.
# l = ["Sunidhi", "Pranjal", "janu", "Shrishti"]

# for name in l :
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# 3.
# n = int(input("enter your number : "))
# i = 1

# while(i <11):
#     print(f"{n} X {i} = {n*i}")
#     i += 1

# 4.
# n = int(input("enter a number : "))

# for i in range(2, n):
#     if(n%i) == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")

# 5.
# n = int(input("enter your number : "))
# product = 1
# for i in range (1, n+1):
#     product = product * i

# print(product)

# 6.   *
#     ***
#    *****
# n = int(input("enter the number : "))

# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("\n")
 
    # 7.  *
    #     **
    #     ***
# for i in range (1, n+1):
#     print("*"*i, end="")
#     print("")


# 8.  ***
#     * *
#     ***

for i in range(1, n+1):
    if(i == 1 or i== n ):
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")

    print("")