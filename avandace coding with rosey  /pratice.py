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
print("you are trpped in this dungeon and you have to make your way out")
#setting the base vales
number_of_times_though = 0
KEY_NAME_ROOM = "KEY_NAME"
KEY_DISCRIPTION = "KEY_DISCRIPTION"
ENEMY_NAME = "enemy name"
ENEMY_MAX_HEALTH = "ENEMY_MAX_HEALTH"
ENEMY_ATTACK_NAME = "ENEMY_ATTACK_NAME"
ENEMY_HIT_CHANCE = "ENEMY_HIT_CHANCE"
ENEMY_DAMAGE = "ENEMY_DAMAGE"
PLAYER_ATTACK_NAME = "PLAYER_ATTACK_NAME"
PLAYER_ATTACK_DAM = "PLAYER_ATTACK_DAM"
PLAYER_ATTACK_CHANCE = "PLAYER_ATTACK_CHANCE"
max_hitpoints = 200
bludgeon_dam = 10
bludgeon_attack_chance = 60
shiv_dam = 5
shiv_attack_chance= 90
punch_dam = 7
punch_attack_chance = 80
shoot_with_bow_dam = 20
shoot_with_bow_attack_chance = 50
your_current_health = max_hitpoints


def fight_room(your_current_health,bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance ):
    print("fight room")
    user_attacks = [
        {PLAYER_ATTACK_NAME: "bludgeon",PLAYER_ATTACK_DAM: bludgeon_dam,PLAYER_ATTACK_CHANCE: bludgeon_attack_chance},
        {PLAYER_ATTACK_NAME: "shiv",PLAYER_ATTACK_DAM: shiv_dam,PLAYER_ATTACK_CHANCE: shiv_attack_chance},
        {PLAYER_ATTACK_NAME: "punch",PLAYER_ATTACK_DAM: punch_dam,PLAYER_ATTACK_CHANCE: punch_attack_chance},
        {PLAYER_ATTACK_NAME: "shoot at them with a bow", PLAYER_ATTACK_DAM: shoot_with_bow_dam,PLAYER_ATTACK_CHANCE: shoot_with_bow_attack_chance}
    ]
    enemytofight = [
        {ENEMY_NAME: "Devil",ENEMY_MAX_HEALTH: 200,ENEMY_ATTACK_NAME: "whips",ENEMY_DAMAGE: 15,ENEMY_HIT_CHANCE: 60},
        {ENEMY_NAME: "Giant",ENEMY_MAX_HEALTH: 150,ENEMY_ATTACK_NAME: "punchs",ENEMY_DAMAGE: 20,ENEMY_HIT_CHANCE: 50},
        {ENEMY_NAME: "Spider",ENEMY_MAX_HEALTH: 50,ENEMY_ATTACK_NAME:  "shoots webs at",ENEMY_DAMAGE: 5,ENEMY_HIT_CHANCE: 90},
        {ENEMY_NAME: "Orc",ENEMY_MAX_HEALTH: 100,ENEMY_ATTACK_NAME: "stabs",ENEMY_DAMAGE: 10,ENEMY_HIT_CHANCE: 80},
        {ENEMY_NAME: "Thing",ENEMY_MAX_HEALTH: 150,ENEMY_ATTACK_NAME: "barfs on", ENEMY_DAMAGE: 10,ENEMY_HIT_CHANCE: 70}
    ]

    chosen_enemy = random.choice(enemytofight)
    chosen_enemy_current_health = chosen_enemy[ENEMY_MAX_HEALTH]
    

    print(f"you walked in to the room and a {chosen_enemy[ENEMY_NAME]} is there \n get ready to fight")
    while True:
        while True:
            print("here are your attacks please answer in nubers")
            for i,j in enumerate(user_attacks):
                print(f"{i + 1}. {j[PLAYER_ATTACK_NAME]} damage is {j[PLAYER_ATTACK_DAM]} hit chance is {j[PLAYER_ATTACK_CHANCE]}%")
            user_pick = input()
            try:
                user_pick = int(user_pick)
                if user_pick not in (1,2,3,4):
                    print("invaild answer")
                    continue
                else:
                    break
            except:
                print("invild answer")
                continue
        print(f"the {chosen_enemy[ENEMY_NAME]} {chosen_enemy[ENEMY_ATTACK_NAME]} you")
        user_pick -= 1
        your_attack_chance = random.uniform(1,100)
        if your_attack_chance < user_attacks[user_pick][PLAYER_ATTACK_CHANCE]:
            chosen_enemy_current_health -= user_attacks[user_pick][PLAYER_ATTACK_DAM]
            print(f"you hit {chosen_enemy[ENEMY_NAME]} and did {user_attacks[user_pick][PLAYER_ATTACK_DAM]} damage.The {chosen_enemy[ENEMY_NAME]} has {chosen_enemy_current_health} health left")
        else:
            print(f"you missed the {chosen_enemy[ENEMY_NAME]}")
        if chosen_enemy_current_health <= 0:
            print(f"good job you beat the {chosen_enemy[ENEMY_NAME]}")
            return your_current_health
        enemy_attack_chance = random.uniform(1,100)
        if enemy_attack_chance < chosen_enemy[ENEMY_HIT_CHANCE]:
            your_current_health -= chosen_enemy[ENEMY_DAMAGE]
            print(f"you have {your_current_health}/{max_hitpoints}")
        else:
            print(f"the {chosen_enemy[ENEMY_NAME]} missed")
        if your_current_health <= 0:
            print(f"you lost")
            sys.exit()

def health_room(your_current_health):
    print("you walk into the room and a fountain in is the middle of the room")
    health_yes_or_no = input("do you want to drink from the fountain yes/no \n").strip().upper()
    if health_yes_or_no in ("YES", "Y"):
        print("you drunk from the fountain and feel refreshed you gain 50 health")
        your_current_health += 50
    else:
        print("you walk past and exit the room")
    return your_current_health

def hard_fight(your_current_health):
    print("fight room")
    user_attacks = [
        {PLAYER_ATTACK_NAME: "bludgeon",PLAYER_ATTACK_DAM: bludgeon_dam,PLAYER_ATTACK_CHANCE: bludgeon_attack_chance},
        {PLAYER_ATTACK_NAME: "shiv",PLAYER_ATTACK_DAM: shiv_dam,PLAYER_ATTACK_CHANCE: shiv_attack_chance},
        {PLAYER_ATTACK_NAME: "punch",PLAYER_ATTACK_DAM: punch_dam,PLAYER_ATTACK_CHANCE: punch_attack_chance},
        {PLAYER_ATTACK_NAME: "shoot at them with a bow", PLAYER_ATTACK_DAM: shoot_with_bow_dam,PLAYER_ATTACK_CHANCE: shoot_with_bow_attack_chance}
    ]
    enemytofight = [
        {ENEMY_NAME: "Kraken",ENEMY_MAX_HEALTH: 300,ENEMY_ATTACK_NAME: "picks you up and drops",ENEMY_DAMAGE:30 ,ENEMY_HIT_CHANCE: 70},
        {ENEMY_NAME: "Leviathan",ENEMY_MAX_HEALTH: 200,ENEMY_ATTACK_NAME: "bites",ENEMY_DAMAGE: 25,ENEMY_HIT_CHANCE: 80},
        {ENEMY_NAME: "Hydra",ENEMY_MAX_HEALTH: 300,ENEMY_ATTACK_NAME:  "spits acid at you",ENEMY_DAMAGE: 30,ENEMY_HIT_CHANCE: 70},
        ]

    chosen_enemy = random.choice(enemytofight)
    chosen_enemy_current_health = chosen_enemy[ENEMY_MAX_HEALTH]
    

    print(f"you walked in to the room and a {chosen_enemy[ENEMY_NAME]} is there \n get ready to fight")
    while True:
        while True:
            print("here are your attacks please answer in nubers")
            for i,j in enumerate(user_attacks):
                print(f"{i + 1}. {j[PLAYER_ATTACK_NAME]} damage is {j[PLAYER_ATTACK_DAM]} hit chance is {j[PLAYER_ATTACK_CHANCE]}%")
            user_pick = input()
            try:
                user_pick = int(user_pick)
                if user_pick not in (1,2,3,4):
                    print("invaild answer")
                    continue
                else:
                    break
            except:
                print("invild answer")
                continue
        print(f"the {chosen_enemy[ENEMY_NAME]} {chosen_enemy[ENEMY_ATTACK_NAME]} you")
        user_pick -= 1
        your_attack_chance = random.uniform(1,100)
        if your_attack_chance < user_attacks[user_pick][PLAYER_ATTACK_CHANCE]:
            chosen_enemy_current_health -= user_attacks[user_pick][PLAYER_ATTACK_DAM]
            print(f"you hit {chosen_enemy[ENEMY_NAME]} and did {user_attacks[user_pick][PLAYER_ATTACK_DAM]} damage.The {chosen_enemy[ENEMY_NAME]} has {chosen_enemy_current_health} health left")
        else:
            print(f"you missed the {chosen_enemy[ENEMY_NAME]}")
        if chosen_enemy_current_health <= 0:
            print(f"good job you beat the {chosen_enemy[ENEMY_NAME]}")
            return your_current_health
        enemy_attack_chance = random.uniform(1,100)
        if enemy_attack_chance < chosen_enemy[ENEMY_HIT_CHANCE]:
            your_current_health -= chosen_enemy[ENEMY_DAMAGE]
            print(f"you have {your_current_health}/{max_hitpoints}")
        else:
            print(f"the {chosen_enemy[ENEMY_NAME]} missed")
        if your_current_health <= 0:
            print(f"you lost")
            sys.exit()

def health_room(your_current_health):
    print("you walk into the room and a fountain in is the middle of the room")
    health_yes_or_no = input("do you want to drink from the fountain yes/no \n").strip().upper()
    if health_yes_or_no in ("YES", "Y"):
        print("you drunk from the fountain and feel refreshed you gain 50 health")
        your_current_health += 50
    else:
        print("you walk past and exit the room")
    return your_current_health


def gambling_room(your_current_health):
    print("you walk into the room and a altar is the middle of the room")
    print("do you want to use the altar yes/no")
    gambling_yes_or_no = input().strip().upper() 
    if gambling_yes_or_no in ("YES","Y"):
        while True:
            print("how much health do you want to put up")
            how_much_health = input()
            try:
                how_much_health = int(how_much_health)
                if how_much_health > your_current_health:
                    print("invaild answer")
                    continue
                else:
                    break
            except:
                continue
        chance_of_losing = random.random()
        if chance_of_losing > 0.5:
            your_current_health += how_much_health
            print("you won and doubled the health you put up")
            print(f"you have {your_current_health}")
            return your_current_health
        elif chance_of_losing < 0.5:
            your_current_health -= how_much_health
            print(f"you gambled and lost {how_much_health} health")
            print(f"you have {your_current_health}")
            return your_current_health
    else:
        print("you leave the room")

def upgrade_room(bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance):
    print("you walk into the room and there is an anvil in the middle on it")
    user_upgrade = input("do you want to use it yes/no").strip().upper()
    if user_upgrade in ("YES","Y"):
        while True:
            what_to_upgrade = input("what do you want to upgrade \n damage \n accuracy ").strip().upper()
            if what_to_upgrade == "DAMAGE":
                while True:
                    print("what do you want to upgrade (please answer in numbers)")
                    print("1.bludgeon damage \n 2.shiv damage \n 3.punch damage \n 4.bow damage")
                    which_one = input()
                    try:
                        which_one = int(which_one)
                        break
                    except:
                        print("invaild answer")
                        continue
                if which_one == 1:
                    bludgeon_dam += 10
                    print("bludgeon now does 10 extra damage")
                    print("you walk out of the room to the next one")
                    return bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance
                elif what_to_upgrade == 2:
                    shiv_dam += 5
                    print("shiv now does 5 extra damage")
                    print("you walk out of the room to the next one")
                    return bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance
                elif which_one == 3:
                    punch_dam += 14
                    print("punch now does 7 extra damage")
                    print("you walk out of the room to the next one")
                    return bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance
                elif which_one == 4:
                    shoot_with_bow_dam += 20
                    print("bow now does 20 extra damage")
                    print("you walk out of the room to the next one")
                    return bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance
            if what_to_upgrade == "ACCURACY":
                while True:
                    print("what do you want to upgrade (please answer in numbers)")
                    print("1.bludgeon accuracy \n 2.shiv accuracy \n 3.punch accuracy \n 4.bow accuracy")
                    which_one = input()
                    try:
                        which_one = int(which_one)
                        break
                    except:
                        print("invaild answer")
                        continue
                if which_one == 1:
                    bludgeon_attack_chance += 10
                    print(f"bludgeon now has {bludgeon_attack_chance}%")
                    print("you walk out of the room to the next one")
                    return bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance
                elif what_to_upgrade == 2:
                    shiv_attack_chance += 10
                    print(f"shiv now has {shiv_attack_chance}%")
                    print("you walk out of the room to the next one")
                    return bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance
                elif which_one == 3:
                    punch_attack_chance += 10
                    print(f"punch now has {punch_attack_chance}%")
                    print("you walk out of the room to the next one")
                    return bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance 
                elif which_one == 4:
                    shoot_with_bow_attack_chance += 10
                    print(f"bow now has {shoot_with_bow_attack_chance}%")
                    print("you walk out of the room to the next one")
                    return bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance
            else:
                print("invaild answer")
                continue


print("you are trpped in this dungeon and you have to make your way out")
number_of_times_though = 0
KEY_NAME = "KEY_NAME"
KEY_DISCRIPTION = "KEY_DISCRIPTION"
while number_of_times_though <= 15:

    rooms = [
        {KEY_NAME:"A big room", KEY_DISCRIPTION:"the exit on the other side has bars on it"},
        {KEY_NAME:"A small room", KEY_DISCRIPTION:"has an anvil in the middle of it"},
        {KEY_NAME:"A very big room", KEY_DISCRIPTION:"looks like there is something diffferent about it"},
        {KEY_NAME: "A median room", KEY_DISCRIPTION:"A fountain stands in the middle "},
        {KEY_NAME: "A median roomm", KEY_DISCRIPTION: "A altar stands in the middle"}
        ]
    chosen_room1 = random.choice(rooms)
    chosen_room2 = random.choice(rooms)
    
    while True:
        which_room = input(f"what room do you want to pick \n 1.{chosen_room1[KEY_NAME]} - {chosen_room1[KEY_DISCRIPTION]} \n 2.{chosen_room2[KEY_NAME]} - {chosen_room2[KEY_DISCRIPTION]} \n").strip()
        try:
            which_room = int(which_room)
            if which_room not in (1,2):
                print("invaild answer")
                continue
            else:
                break
        except:
            print("invaild answer")
            continue
    
    if which_room == 1:
        if chosen_room1[KEY_NAME] == rooms[0][KEY_NAME]:
            your_current_health = fight_room(your_current_health,bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance)
            number_of_times_though += 1
            continue
        elif chosen_room1[KEY_NAME] == rooms[1][KEY_NAME]:
            bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance = upgrade_room(bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance)
            number_of_times_though += 1
            continue
        elif chosen_room1[KEY_NAME] == rooms[2][KEY_NAME]:
            your_current_health = hard_fight(your_current_health)
            
            bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance = upgrade_room(bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance)
            number_of_times_though += 1
        elif chosen_room1[KEY_NAME] == rooms[3][KEY_NAME]:

            your_current_health = health_room(your_current_health)
            number_of_times_though += 1
            continue
        elif chosen_room1[KEY_NAME] == rooms[4][KEY_NAME]:
            your_current_health = gambling_room(your_current_health)

    elif which_room == 2:
        if chosen_room2[KEY_NAME] == rooms[0][KEY_NAME]:
            your_current_health = fight_room(your_current_health,bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance)
            number_of_times_though += 1
            continue
        elif chosen_room2[KEY_NAME] == rooms[1][KEY_NAME]:
            bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance = upgrade_room(bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance)
            
            number_of_times_though += 1
            continue
        elif chosen_room2[KEY_NAME] == rooms[2][KEY_NAME]:
            your_current_health = hard_fight(your_current_health)
        
            
            bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance = upgrade_room(bludgeon_dam,bludgeon_attack_chance,shiv_dam,shiv_attack_chance,punch_dam,punch_attack_chance,shoot_with_bow_dam,shoot_with_bow_attack_chance)
            number_of_times_though += 1
        elif chosen_room2[KEY_NAME] == rooms[3][KEY_NAME]:
            your_current_health = health_room(your_current_health)
            number_of_times_though += 1
            continue
        elif chosen_room1[KEY_NAME] == rooms[4][KEY_NAME]:
            your_current_health = gambling_room(your_current_health)






