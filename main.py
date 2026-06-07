



#name = input ("Name?\n")
#print("hello "+name)
#print("Good to know you are " +input(f"how are you {name}?\n"))

#print(6 * 5.0)

#name = "sonny"
#age = 15
#print(name, "is", age)


#age = 5
#print("He is " + str(age))



#age = input("Age?")
#print("birth year:", 2026 - int(age))


# print(5 + 5 == 10)
"""
print(5 + 5 == 8)
print(5 == 5.0)
print("hello" == "hi")
print(5 + 5 >=10)
print(5 + 5 >= 8)
print(5 != 5)
print(5 != 6)
print("hello" != "hi")
print(5 == "5")
"""
"""
if 5 < 10:
    print("hello")
if 5 < 10:
    pass

if 10 != 10:
    print("hello")
print ("goodbye")
"""

"""

if 5< 10 :
    print("less than 10")
else:
    print("10 or more ")




print("hello".upper())
print("HELLO".lower())

if "HELLO".lower() == "hello":
    print("The same!")



guess = input("what's the  password ")
print("checking password is a match")
while guess != "secret":
    guess = input("try again ")
    print("checking password is a match")
input("welcome")

"""

"""
import random
print(random.random())
print(random.randint(0,10))
"""



user_input = "idk"
try:
    num = int(user_input)
    print(f"you picked {num}")
except:
    print(f"{user_input} is not a number")