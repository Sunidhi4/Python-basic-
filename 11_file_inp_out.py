# f = open("file.txt")
# print(data)
# f.close()

# f = open("file.txt", "w")
# st = "Gangstar "
# data = f.write(st)

# f = open("file.txt", "a")
# st = "Gangstar "
# data = f.write(st)

# f = open("file.txt")

# lines = f.readlines()

# print(lines, type(lines))

# f.close()


# practice set 
# 1.
# f = open("file.txt")
# content = f.read()
# if("twinkle" in content ):
#     print("the word twinkle is present in the content")

# else:
#     print("the word twinkle is not present in the content")

import random 

def game():
    print("you are playing the game...")
    score = random.randint(1,62)
    # fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
          hiscore = int(hiscore)
        else:
           hiscore = 0

        
    print("your score : ", score)
    if(score > hiscore ):
    #   write this hiscore to the file 
     with open("hiscore.txt", "w") as f :
       f.write(str(score))

    return score


game()