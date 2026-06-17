



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

"""

user_input = "idk"
try:
    num = int(user_input)
    print(f"you picked {num}")
except:
    print(f"{user_input} is not a number")
    """

"""
count = 0 
while count < 10:
    print("counting...")
    if count < 5:
        continue
    print("almost done..")
print("finshed")


while True:
    guess = input("guess a country ")
    if guess.lower().strip() == "malawi":
        break
    print("try again")
print("well done")

import random
shopping_list = ["apples", "plums", "pizza"]
print(shopping_list[random.randint(0,2)])
"""

"""
shopping_list = ['apples', 'oranges','melons']
print(shopping_list)
shopping_list.append('carrots')
shopping_list.remove('oranges')
print(shopping_list)
shopping_list.pop(0)
shopping_list.insert(1, "apples")
print(shopping_list)
shopping_list.sort()
print(shopping_list)



shopping_list = ['apples','plums','pizza']
print('apples' in shopping_list)

print('a' in 'definitely')


user_input = input()
if user_input.lower() in['a','b','c','d']:
	print('Checking answer…')
else:
	print('That’s not a valid answer!')
"""

"""
print(len('apples'))

shopping_list = ['apples','plums','pizza']
print(len(shopping_list))

shopping_list = ['apples','plums','pizza']
print(len(shopping_list[1]))

if len(input()) == 0:
    print("You didn't type anything")
"""
"""
for food in ['apples','carrots','muesli']:
    print(food)

for i in range(10):
    print("Hello\n")

foods = ['apples','carrots','muesli']
for i in range(len(foods)):
    print(f'{i+1}.{foods[i]}')

counter = 1
while counter < 4:
    print("Looping!")
    counter = counter + 1


"""
"""
fruit = [
    {"name":"apples", "calories":52},
    {"name":"oranges", "calories":47},
    {"name":"pears", "calories":57},
    {"name":"bananas", "calories":89},
    {"name":"strawberries", "calories":32},
    {"name":"grapes", "calories":68},
    {"name":"blueberries", "calories":57},
    {"name":"pineapples", "calories":50},
    {"name":"kiwifruit", "calories":61},
    {"name":"watermelon", "calories":30}
]

print(fruit[3]["name"])




KEY_NAME = "name"
KEY_CALORIES = "calories"

fruit = [
    {KEY_NAME:"apples", KEY_CALORIES:52},
    {KEY_NAME:"oranges", KEY_CALORIES:47},
    {KEY_NAME:"pears", KEY_CALORIES:57},
    {KEY_NAME:"bananas", KEY_CALORIES:89},
    {KEY_NAME:"strawberries", KEY_CALORIES:32},
    {KEY_NAME:"grapes", KEY_CALORIES:68},
    {KEY_NAME:"blueberries", KEY_CALORIES:57},
    {KEY_NAME:"pineapples", KEY_CALORIES:50},
    {KEY_NAME:"kiwifruit", KEY_CALORIES:61},
    {KEY_NAME:"watermelon", KEY_CALORIES:30}
]
print(fruit[3][KEY_CALORIES])
"""
