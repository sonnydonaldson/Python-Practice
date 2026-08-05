import random
import sys 
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

number_of_times_though = 0
KEY_NAME_ROOM = "KEY_NAME"
KEY_DISCRIPTION = "KEY_DISCRIPTION"
ENEMY_NAME = "ENEMY_NAME"
ENEMY_MAX_HEALTH = "ENEMY_MAX_HEALTH"
ENEMY_ATTACK_NAME = "ENEMY_ATTACK_NAME"
ENEMY_DAMAGE = "ENEMY_DAMAGE"
ENEMY_HIT_CHANCE = "ENEMY_HIT_CHANCE"
PLAYER_ATTACK_NAME = "PLAYER_ATTACK_NAME"
PLAYER_ATTACK_DAM = "PLAYER_ATTACK_DAM"
PLAYER_ATTACK_CHANCE = "PLAYER_ATTACK_CHANCE"
bludgeon_dam = 10
bludgeon_attack_chance = 60
shiv_dam = 5
shiv_attack_chance= 90
punch_dam = 7
punch_attack_chance = 80
shoot_with_bow_dam = 20
shoot_with_bow_attack_chance = 50
your_current_health = 200

def hard_fight_room(your_current_health, bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance):
    print("fight room")
    #listing the attacks the users can use
    user_attacks = [
        {PLAYER_ATTACK_NAME: "blugeon", PLAYER_ATTACK_DAM: bludgeon_dam, PLAYER_ATTACK_CHANCE: bludgeon_attack_chance},
        {PLAYER_ATTACK_NAME: "shiv", PLAYER_ATTACK_DAM: shiv_dam, PLAYER_ATTACK_CHANCE: shiv_attack_chance},
        {PLAYER_ATTACK_NAME: "punch", PLAYER_ATTACK_DAM: punch_dam, PLAYER_ATTACK_CHANCE: punch_attack_chance},
        {PLAYER_ATTACK_NAME: "shoot at them with bow", PLAYER_ATTACK_DAM: shoot_with_bow_dam, PLAYER_ATTACK_CHANCE: shoot_with_bow_attack_chance}
        ]
    #list the different enemys for hard fights
    enemytofight = [
        {ENEMY_NAME: "Kraken", ENEMY_MAX_HEALTH: 300, ENEMY_ATTACK_NAME: "picks you up and drops", ENEMY_DAMAGE: 30, ENEMY_HIT_CHANCE: 70},
        {ENEMY_NAME: "Leviathan", ENEMY_MAX_HEALTH: 200, ENEMY_ATTACK_NAME: "bites", ENEMY_DAMAGE: 25, ENEMY_HIT_CHANCE: 80},
        {ENEMY_NAME: "Hydra", ENEMY_MAX_HEALTH: 300, ENEMY_ATTACK_NAME: "spits acid at you", ENEMY_DAMAGE: 30, ENEMY_HIT_CHANCE: 70}
        ]
    #randomly chosing an enemy
    chosen_enemy = random.choice(enemytofight)
    chosen_enemy_current_health = chosen_enemy[ENEMY_MAX_HEALTH]

    #telling you what enemy is there and telling you your attacks
    print(f"you walked into the room and a {chosen_enemy[ENEMY_NAME]} is there \n get ready to fight")
    while True:
        while True: 
            print("here are you attacks please answer in numbers")
            for i,j in enumerate(user_attacks):
                print(f"{i + 1}. {j[PLAYER_ATTACK_NAME]} damage is {j[PLAYER_ATTACK_DAM]} hit chance is {j[PLAYER_ATTACK_NAME]}")
                user_pick = input()
            #checking that it is a viable answer
            try:
                user_pick = int(user_pick)
                if user_pick not in (1,2,3,4):
                    print("invaild answer")
                    continue
                else:
                    break
            except:
                print("invaild answer")
                continue
        #telling you what attack the enemy used 
        print(f" {chosen_enemy[ENEMY_NAME]} {chosen_enemy[ENEMY_ATTACK_NAME]}")
        #getting the values for your attacks
        user_pick -= 1
        you_attack_chance = random.uniform(1,100)
        #seeing if you hit the enemy and if so taking away some of its health
        if you_attack_chance < user_attacks[user_pick][PLAYER_ATTACK_CHANCE]:
            chosen_enemy_current_health -= user_attacks[user_pick][PLAYER_ATTACK_DAM]
            print(f"you hit the {chosen_enemy[ENEMY_NAME]} and did {user_attacks[user_pick][PLAYER_ATTACK_DAM]} damage. The {chosen_enemy[ENEMY_NAME]} has {chosen_enemy_current_health} health left")
        else: 
            print("you missed")
        if chosen_enemy_current_health <= 0:
            print(f"good job you beat the {chosen_enemy[ENEMY_NAME]}")
            return your_current_health
        #seeing if the enemy hit you and taking away your health
        enemy_attack_chance = random.uniform(1,100)
        if enemy_attack_chance < chosen_enemy[ENEMY_HIT_CHANCE]:
            your_current_health -= chosen_enemy[ENEMY_DAMAGE]
            print(f"you have {your_current_health} left")
        else:
            print(f"the {chosen_enemy[ENEMY_NAME]} missed")
        #cheaking if you die
        if your_current_health <= 0:
            print("you lost")
            sys.exit()


