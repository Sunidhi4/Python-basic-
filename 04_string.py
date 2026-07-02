# name = "Harry"

# # string slicing
# nameshort = name[0:3] #start from index 0 all the way till 3 (excluding 3)
# print(nameshort)
# print(name[-4:-1])
# print(name[1:4])
# print(name[:4]) #[0:4]
# print(name[1:]) #[1:5]
# print(name[1:5])

# #slicing with skip value
# word = "amazing"
# print(word[1:6:2])

# #string function

# print(len(name))
# print(name.endswith("rry"))
# print(name.startswith("ha"))
# print(name.capitalize())
# print(name.count('r'))
# print(name.find('y'))
# print(name.replace("arry", "auuy"))

# # escape sequence character
# d = "I am \"done with this\" \n but i am doing it "

# print(d)

#  practice set 
# 1. 
# name = input("enter your name : ")
# print (f"good afternoon {name} ")

# # 2. 
letter = '''Dear <|Name|>,
You are selected 
<|Date|>'''

print(letter.replace("<|Name|>", "Sunidhi").replace("<|Date|>","15 december 2025"))

# # 3.
# name = "I don't  know  what to do"
# print (name.replace("  ", " "))
#  Strings are immutable which means that you cannot change them by running functions on them