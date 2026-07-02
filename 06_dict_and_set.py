# dictionary : dictionary is a collection of key value pairs.
# Properties of dictionary : 1. It is uunordered.
# 2. It is mutable.
# 3. It is indexed
# 4. Cannot contains duplicate keys.

#d = {} empty dictionary

marks = {
    "Sunidhi" : 7.83,
    "Shrishti" : 7.3,
    "Ritu" : 6.0
}
#  marks.item() : Returns a list of (key, value)tuples.
# marks.keys() : Returns a list containing dictionary's keys.
# marks.update({"friends : "}) : Upadates the dictionary with supplied key-value pairs.
# marks.get("name") : Returns the value of the specific keys (and value is returned).


# print(marks, type(marks))
# print(marks["Ritu"])

# print(marks.items())  #dict_items[('sunidhi',7.83),('shristi',7.3),('Ritu',6.0)]
# print(marks.keys())   #dict_keys(['Sunidhi', 'Shrishti','Ritu'])
# print(marks.values()) #dict_values([7.83, 7.3, 6.0])
marks.update({"Sunidhi": 8.5, "Pihu" : 7.6})
print(marks)
print(marks.get("Sunidhi2"))  #return none
# print(marks["sunidhi2"])  #return error

#Set : Set is a collection of non-repetitive elements.

# e = set() #empty set
s = {6, 8 ,90, "googly"}
# s.add(89)
# print(s)

# Properties of sets:
# 1. Sets are unordered => Element's order doesn't matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contains duplicate values.

# methods : 1. len(s) : Retirns the length of a set .
# 2. s.remove(8) : Updates the set s and remove 8 from set.
# 3. s.pop() : Remove an arbitary element from the set and return the elements removed .
# 4. s.clear() : empties the set s.
# 5. s.union(8,11) : Returns the new set with all the items from both sets. {1,2,8,3,11}
# 6. s.intersection(8, 11) : Returns a set which contains only items in both sets {8}.

# s.remove(8)
# print(s)
 
# s1 = {1, 45, 78, 6}
# s2 = {7, 8, 1, 78}

# print(s1.union(s2))
# print(s1.intersection(s2))
# print({1,45}.issubset(s1))
# print(s1.issuperset({1,6}))

# practice set 
# 1. 
# words = {
#     "Help" : "Madad",
#     "cat" : "Billi",
#     "crony" : "ajib"
# }

# word = input("enter the owrd you want meaning : ")

# print(words.get(word))

# 2.
# numbers = set()

# n1 = input("enter the 1 number : ")
# numbers.add(n1)
# n2 = input("enter the 2 number : ")
# numbers.add(n2)
# n3 = input("enter the 3 number : ")
# numbers.add(n3)
# n4 = input("enter the 4 number : ")
# numbers.add(n4)
# n5 = input("enter the 5 number : ")
# numbers.add(n5)
# n6 = input("enter the 6 number : ")
# numbers.add(n6)
# n7 = input("enter the 7 number : ")
# numbers.add(n7)
# n8 = input("enter the 8 number : ")
# numbers.add(n8)

# print(numbers)

# 3. 
# d= {}

# name = input("enter friends name : ")
# lang = input("enter language name : ")
# d.update({name : lang})
# name = input("enter friends name : ")
# lang = input("enter language name : ")
# d.update({name : lang})
# name = input("enter friends name : ")
# lang = input("enter language name : ")
# d.update({name : lang})
# name = input("enter friends name : ")
# lang = input("enter language name : ")
# d.update({name : lang})

# print(d)

# 4.
# s = {8, 7, 12, "Harry", [1,2]}  set should be immutable and hashable 