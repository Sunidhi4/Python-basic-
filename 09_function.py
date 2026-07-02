# function defination
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c)/3
    print(average)

# function call
# avg()

def goodDay(name, ending="thank you"):
    print("Good Day " +name) 
    print(ending)
    return "done"

a = goodDay("Sunidhi")
print(a)