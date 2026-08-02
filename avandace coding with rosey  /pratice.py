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
#setting the base vales
number_of_times_though = 0
KEY_NAME_ROOM = "KEY_NAME"
KEY_DISCRIPTION = "KEY_DISCRIPTION"
max_hitpoints = 200
bludgeon_dam = 10
bludgeon_attack_chance = 60
shiv_dam = 5
shiv_attack_chance= 90
punch_dam = 7
punch_attack_chance = 80
shoot_with_bow_dam = 20
shoot_with_bow_attack_chance = 50
  

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
            user_attacks = [
                {"bludgeon", bludgeon_dam, bludgeon_attack_chance},
                {"shiv", shiv_dam, shiv_attack_chance},
                {"punch", punch_dam,punch_attack_chance},
                {"shoot at them with a bow",shoot_with_bow_dam, shoot_with_bow_attack_chance}
            ]
            enemytofight = [
                {"Devil", "200", "whips", "15", "60"},
                {"Giant", "150", "punchs", "20", "50"},
                {"Spider", "50", "shoots webs at", "5", "90"},
                {"Orc", "100", "stabs", "10", "80"},
                {"Thing", "150", "barfs on", "10","70"}
            ]

            chosen_enemy = random.choice(enemytofight)
            chosen_enemy_current_health = chosen_enemy[1]
            your_current_health = max_hitpoints

            print(f"you walked in to the room and a {chosen_enemy[0]} is there \n get ready to fight")
            while True:
                print("here are your attacks please answer in nubers")
                for i,j in enumerate(user_attacks):
                    print(f"{i + 1}. {j[0]} damage is {j[1]} hit chance is {j[2]}%")
                    user_pick = input()
                try:
                    user_pick = int(user_pick)
                    break
                except:
                    print("invild answer")
                    continue
            while True:
                print(f"the {chosen_enemy[0]} {chosen_enemy[2]} you")
                user_pick -= 1
                your_attack_chance = random.uniform(1,100)
                if your_attack_chance < user_attacks[user_pick][2]:
                    chosen_enemy_current_health -= user_attacks[user_pick][1]
                    print(f"you hit {chosen_enemy[0]} and did {user_attacks[user_pick][1]} damage.The {chosen_enemy[0]} has {chosen_enemy_current_health} health left")
                else:
                    print(f"you missed the {chosen_enemy[0]}")
                if chosen_enemy_current_health <= 0:
                    print(f"good job you beat the {chosen_enemy[0]}")
                    break
                enemy_attack_chance = random.uniform(1,100)
                if enemy_attack_chance < chosen_enemy[4]:
                    your_current_health -= chosen_enemy[3]
                    print(f"you have {your_current_health}/{max_hitpoints}")
                else:
                    print(f"the {chosen_enemy[0]} missed")
                if your_current_health <= 0:
                    print(f"you lost")
                    break
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






#defining a fight room


