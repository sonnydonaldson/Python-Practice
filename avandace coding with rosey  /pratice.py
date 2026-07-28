import random




"""
eRelease = True
while True:
    if keyboard.is_pressed("e") and eRelease:
        print("Yellow")
        eRelease = False

    elif not keyboard.is_pressed("e"):
        eRelease = True
"""
"""
name = input("hello what is your name ").upper().strip()

def makesomething():  
    if name != "SONNY":
        return "good"
    else:
        return "bad"
answer = makesomething()

print(f"{answer}")

"""
"""
class person():
    def __init__(self,iframe,hframe):
        self.iframe = iframe
        self.hframe = hframe
        

sonny = person("hi", "sonny")
print(sonny.iframe + sonny.hframe)

"""
"""
class room():
    def __init__(self, name):
        self.name = name

    def describeRoom(self):
        print(f"{self.name} - A dusty old room")

class combatRoom(room):
    def __init__(self, name, enemy):
        super().__init__(name)
        self.enemy = enemy

    def describeRoom(self):
        print(f"{self.name} - Contains {self.enemy}")

class shopRoom(room):
    def __init__(self, name, forSale):
        super().__init__(name)
        self.forSale = forSale

    def item(self):
        print(f"The item {self.forSale} is for sale")

rooms = [
    room("Cabin"),
    combatRoom("Dungeon", "Vampire"),
    shopRoom("Shop", "Sword")
]
chosenRoom = random.choice(rooms)
chosenRoom.describeRoom()
if type(chosenRoom) is shopRoom:
    chosenRoom.item()


"""

        

print("you are trpped in this dungeon and you have to make your way out")
number_of_times_though = 0
KEY_NAME = "KEY_NAME"
KEY_DISCRIPTION = "KEY_DISCRIPTION"
while number_of_times_though <= 15:
    print(f"test {number_of_times_though}")
    rooms = [
        {KEY_NAME:"A big room", KEY_DISCRIPTION:"the exit on the other side has bars on it"},
        {KEY_NAME:"A small room", KEY_DISCRIPTION:"has an anvil in the middle of it"},
        {KEY_NAME:"A very big room", KEY_DISCRIPTION:"looks like there is something diffferent about it"},
        {KEY_NAME: "A median room", KEY_DISCRIPTION:"An altar stands in the middle "}
        ]
    chosen_room1 = random.choice(rooms)
    chosen_room2 = random.choice(rooms)
    
    while True:
        which_room = input(f"what room do you want to pick \n 1.{chosen_room1[KEY_NAME]} - {chosen_room1[KEY_DISCRIPTION]} \n 2.{chosen_room2[KEY_NAME]} - {chosen_room2[KEY_DISCRIPTION]} \n").strip()
        try:
            which_room = int(which_room)
            break
        except:
            print("invaild answer")
            continue
    if which_room == 1:
        if chosen_room1[KEY_NAME] == rooms[0][KEY_NAME]:
            print("fight room")
            #call fight room 5
            number_of_times_though += 1
        elif chosen_room1[KEY_NAME] == rooms[1][KEY_NAME]:
            print("upgrade room")
            #call upgrade room
            number_of_times_though += 1
        elif chosen_room1[KEY_NAME] == rooms[2][KEY_NAME]:
            print("hard fight")
            #call hard fight
            number_of_times_though += 1
        elif chosen_room1[KEY_NAME] == rooms[3][KEY_NAME]:
            print("health room")
            #call health room
            number_of_times_though += 1
    elif which_room == 2:
        if chosen_room2[KEY_NAME] == rooms[0][KEY_NAME]:
            print("fight room")
            #call fight room 
            number_of_times_though += 1
        elif chosen_room2[KEY_NAME] == rooms[1][KEY_NAME]:
            print("upgrade room")
            #call upgrade room
            number_of_times_though += 1
        elif chosen_room2[KEY_NAME] == rooms[2][KEY_NAME]:
            print("hard fight")
            #call hard fight
            number_of_times_though += 1
        elif chosen_room2[KEY_NAME] == rooms[3][KEY_NAME]:
            print("health room")
            #call health room
            number_of_times_though += 1

        
