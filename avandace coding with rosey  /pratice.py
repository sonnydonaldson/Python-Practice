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

import random 
import sys

print("you are trpped in this dungeon and you have to make your way out")
#setting the base vales
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

#defining a fight room
def fight_room(your_current_health, bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance):
    print("fight room")
    #listing the attacks the users can use
    user_attacks = [
        {PLAYER_ATTACK_NAME: "blugeon", PLAYER_ATTACK_DAM: bludgeon_dam, PLAYER_ATTACK_CHANCE: bludgeon_attack_chance},
        {PLAYER_ATTACK_NAME: "shiv", PLAYER_ATTACK_DAM: shiv_dam, PLAYER_ATTACK_CHANCE: shiv_attack_chance},
        {PLAYER_ATTACK_NAME: "punch", PLAYER_ATTACK_DAM: punch_dam, PLAYER_ATTACK_CHANCE: punch_attack_chance},
        {PLAYER_ATTACK_NAME: "shoot at them with bow", PLAYER_ATTACK_DAM: shoot_with_bow_dam, PLAYER_ATTACK_CHANCE: shoot_with_bow_attack_chance}
        ]
    #list the different enemys
    enemytofight = [
        {ENEMY_NAME: "Devil", ENEMY_MAX_HEALTH: 200, ENEMY_ATTACK_NAME: "whips", ENEMY_DAMAGE: 15, ENEMY_HIT_CHANCE: 60},
        {ENEMY_NAME: "Giant", ENEMY_MAX_HEALTH: 150, ENEMY_ATTACK_NAME: "punchs", ENEMY_DAMAGE: 20, ENEMY_HIT_CHANCE: 50},
        {ENEMY_NAME: "Spider", ENEMY_MAX_HEALTH: 50, ENEMY_ATTACK_NAME: "shoots webs at", ENEMY_DAMAGE: 5, ENEMY_HIT_CHANCE: 90},
        {ENEMY_NAME: "Orc", ENEMY_MAX_HEALTH: 100, ENEMY_ATTACK_NAME: "stabs", ENEMY_DAMAGE: 10, ENEMY_HIT_CHANCE:80},
        {ENEMY_NAME: "Thing", ENEMY_MAX_HEALTH: 150, ENEMY_ATTACK_NAME: " barfs on", ENEMY_DAMAGE: 10, ENEMY_HIT_CHANCE:70}
        ]
    #randomly chosing an enemy
    chosen_enemy = random.choice(enemytofight)

    chosen_enemy_current_health = chosen_enemy[ENEMY_MAX_HEALTH]

    #telling you what enemy is there and telling you your attacks1

    print(f"you walked into the room and a {chosen_enemy[ENEMY_NAME]} is there \n get ready to fight")
    print(f"you have {your_current_health} health")
    while True:
        while True: 
            print("here are you attacks please answer in numbers")
            for i,j in enumerate(user_attacks):
                print(f"{i + 1}. {j[PLAYER_ATTACK_NAME]} damage is {j[PLAYER_ATTACK_DAM]}. Hit chance is {j[PLAYER_ATTACK_CHANCE]}")
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
        print(f" {chosen_enemy[ENEMY_NAME]} {chosen_enemy[ENEMY_ATTACK_NAME]} you")
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
            print("\n -------------------------------------------------")
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
        print("\n -------------------------------------------------")

#defining a health room
def health_room(your_current_health):
    #giving them imformation
    print("you walk into the room and a fountain is in the middle on the room")
    #asking if they want to drink from the fountion
    while True:
        health_yes_or_no = input("do you want to drink form the fountain yes/no \n").strip().upper()
        if health_yes_or_no in ("YES", "Y"):
            #giving them healtjh because they said yes
            print("you drink from the fountain and feel refreshed you gain 50 health")
            your_current_health += 50
            print("\n -------------------------------------------------")
            return your_current_health
        #skipping it because they said no
        elif health_yes_or_no in ("NO", "N"):
            print("you leave the room")
            print("\n -------------------------------------------------")
            return your_current_health
        else:
            print("inviald answer")
            continue 
    
#defining a hard fight room
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
        {ENEMY_NAME: "Hydra", ENEMY_MAX_HEALTH: 300, ENEMY_ATTACK_NAME: "spits acid at ", ENEMY_DAMAGE: 30, ENEMY_HIT_CHANCE: 70}
        ]
    #randomly chosing an enemy
    chosen_enemy = random.choice(enemytofight)
    chosen_enemy_current_health = chosen_enemy[ENEMY_MAX_HEALTH]

    #telling you what enemy is there and telling you your attacks
    print(f"you walked into the room and a {chosen_enemy[ENEMY_NAME]} is there \n get ready to fight")
    print(f"you have {your_current_health} health")
    while True:
        while True: 
            print("here are you attacks please answer in numbers")
            for i,j in enumerate(user_attacks):
                print(f"{i + 1}. {j[PLAYER_ATTACK_NAME]} damage is {j[PLAYER_ATTACK_DAM]}. Hit chance is {j[PLAYER_ATTACK_CHANCE]}")
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
        print(f" {chosen_enemy[ENEMY_NAME]} {chosen_enemy[ENEMY_ATTACK_NAME]} you")
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
            print("\n -------------------------------------------------")

            return your_current_health
        #seeing if the enemy hit you and taking away your health
        enemy_attack_chance = random.uniform(1,100)
        if enemy_attack_chance < chosen_enemy[ENEMY_HIT_CHANCE]:
            your_current_health -= chosen_enemy["ENEMY_DAMAGE"]
            print(f"you have {your_current_health} left")
        else:
            print(f"the {chosen_enemy[ENEMY_NAME]} missed")
        #cheaking if you die
        if your_current_health <= 0:
            print("you lost")
            sys.exit()
        print("\n -------------------------------------------------")
    
    
#defining upgrade room 
def upgrade_room(bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance):
    #seeing if they want to use 
    print("you walk into the room and there is an anvil in the middle ")
    while True:
        user_upgrade = input("do you want to use it yes/no\n").strip().upper()
        if user_upgrade in ("YES","Y"):
            #if they say yes then it sees if the want to upgrade accuraxcy or damage
            while True:
                what_to_upgrade = input("what do you want to upgrade. \n damage \n accuracy\n").strip().upper()
                if what_to_upgrade == "DAMAGE":
                    while True:
                        #asking them which weapon they want to upgrade
                        print("what do you want to upgrade (please answer in numbers)")
                        print(" 1.bludgeon damage\n 2.shiv damage\n 3.punch damage\n 4.bow damage")
                        which_one = input()
                        #making sure the answer is vaild
                        try:
                            which_one = int(which_one)
                            if which_one not in (1,2,3,4):
                                print("invailded answer")
                                continue
                            else:
                                break
                        except:
                            print("invaild answer")
                            continue
                    #adding damage if they chose bludgeon
                    if which_one == 1:
                        bludgeon_dam += 10
                        print("bludgeon now does 10 extra damage")
                        print("you walk out of the room to the next one")
                        return bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance
                        #adding damage if they chose shiv
                    elif which_one == 2:
                        shiv_dam += 5
                        print("shiv now does 5 extra damage")
                        print("you walk out of the room to the next one")
                        return bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance
                        #adding damage if they chose punch
                    elif which_one == 3:
                        punch_dam += 14
                        print("punching now does 14 extra damage")
                        print("you walk out of the room to the next one")
                        return bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance
                        #adding damage if they chose bow
                    elif which_one == 4:
                        shoot_with_bow_dam += 20
                        print("using the bow now does 20 extra damage")
                        print("you walk out of the room to the next one")
                        return bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance
                        #upgrading there accuracyn if the chose accuracy
                if what_to_upgrade == "ACCURACY":
                    while True:
                        #seeing which one they want to upgrade
                        print("what do you want to upgrade (please answer in numbers)")
                        print(" 1.bludgeon accuracy\n 2.shiv accuracy\n 3.punch accuracy\n 4.bow accuracy")
                        which_one = input()
                        #making sure it is a vailed answer 
                        try:
                            which_one = int(which_one)
                            if which_one not in (1,2,3,4):
                                print("invailded answer")
                                continue
                            else:
                                break
                        except:
                            print("invaild answer")
                            continue
                        #adding accuracy if they chose bludgeon
                    if which_one == 1:
                        bludgeon_attack_chance += 10
                        print(f"bludgeon now has {bludgeon_attack_chance}% hit chance")
                        print("you walk out of the room to the next one")
                        return bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance
                    elif which_one == 2:
                        #adding accuracy if they chose shiv
                        shiv_attack_chance += 10
                        print(f"shiv now has {shiv_attack_chance}% hit chance")
                        print("you walk out of the room to the next one")
                        return bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance
                    elif which_one == 3:
                        #adding accuracy if they chose punch
                        punch_attack_chance += 10
                        print(f"punching now has {punch_attack_chance}% hit chance")
                        print("you walk out of the room to the next one")
                        return bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance
                    elif which_one == 4:
                        #adding accuracy if they chose bow
                        shoot_with_bow_attack_chance += 10
                        print(f"using the bow now has {shoot_with_bow_attack_chance}% hit chance")
                        print("you walk out of the room to the next one")
                        return bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance
                    #resettng it because the answer to what they want to upgrade was wrong
                else:
                    print("invaild answer")
                    continue 
                    
               #skipping everything because they didnt want tpoo upgrade      
        elif user_upgrade in ("NO","N"):
            print("you walk out of the room on to the next one")
            return bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance
            #if they didn't say yes or no it resets
        else:
            print("invaild answer")
            continue
            
def see_how_much_health_they_want_to_put_up(your_current_health):
    while True:
    #asking how much health they want to gamble
        print(f"you have {your_current_health} health")
        print("how much health would you like to put up")
        how_much_health = input().strip()
        #making sure it is a possalbe value 
        try:
            how_much_health = int(how_much_health)
            if how_much_health > your_current_health:
                print("invaild answer")
                continue 
            else:
                return how_much_health
                break
        except:
            print("invaild answer")
            continue
def gambling_health_room(your_current_health):
    #asking them if they want to use it 
    print("you walk into the room and there is an altar is the middle of the room")
    while True:
        print("do you want to use the altar yes/no")
        gambling_yes_or_no = input().strip().upper()
        #gambling if they said yes
        if gambling_yes_or_no in ("YES", "Y"):
            #seeing which odds they would like to go for
            print("would you like to try and double your health or would you like to do the risker")
            print(" one where you quadruple your health but its a lower chance and there is a chanmce you die")
            while True:
                double_or_quadruple = input().strip().upper()
                if double_or_quadruple == "DOUBLE":
                    #seeing how much health they want to put up 
                    how_much_health = see_how_much_health_they_want_to_put_up(your_current_health)
                    #running the gambling chance 
                    chance_of_losing = random.random()
                    #giving you health because you won
                    if chance_of_losing > 0.5:
                        your_current_health += how_much_health
                        print("you won and double the health you put up")
                        print(f"you have {your_current_health}")
                        return your_current_health
                        #taking away your health because you lost
                    elif chance_of_losing < 0.5:
                        your_current_health -= how_much_health
                        print(f"you gambled and lost {how_much_health} health")
                        print(f"you have {your_current_health}")
                        #cheaking if they died
                        if your_current_health <= 0:
                            print("you died")
                            sys.exit()
                        return your_current_health
                elif double_or_quadruple == "QUADRUPLE":
                    #seeing how much health they want to put up 
                    how_much_health = see_how_much_health_they_want_to_put_up(your_current_health)
                    #running the gambling chance
                    chance_of_losing = random.random()
                    
                    if chance_of_losing < 0.2:
                        #quadrupling the health they put up
                        your_current_health += 3*how_much_health
                        print("you won and quadrupled the health you put up")
                        print(f"you have {your_current_health}")
                        return your_current_health
                        #taking away your health because you lost
                    elif chance_of_losing < 0.8 and chance_of_losing > 0.2 :
                        your_current_health -= how_much_health
                        print(f"you gambled and lost {how_much_health} health")
                        print(f"you have {your_current_health}")
                        #cheaking to see if they died
                        if your_current_health <= 0:
                            print("you died")
                            sys.exit()
                        return your_current_health
                    #kiling them because tjhey lost 
                    elif chance_of_losing > 0.8:
                        print("you died")
                        sys.exit()
                #to make sure the code doesnt break
                else:
                    print("invaild answer")
                    continue
        #leaving because they didn't want to do it 
        elif gambling_yes_or_no in ("NO","N"):
                print("you walk out of the room on to the next one")
                return your_current_health
                #if they didn't say yes or no it resets
        else:
            print("invaild answer")
            continue

    
#defining boss fight 

def boss_fight(your_current_health, bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance):
    print("boss fight room")
    #listing the attacks the users can use
    user_attacks = [
        {PLAYER_ATTACK_NAME: "blugeon", PLAYER_ATTACK_DAM: bludgeon_dam, PLAYER_ATTACK_CHANCE: bludgeon_attack_chance},
        {PLAYER_ATTACK_NAME: "shiv", PLAYER_ATTACK_DAM: shiv_dam, PLAYER_ATTACK_CHANCE: shiv_attack_chance},
        {PLAYER_ATTACK_NAME: "punch", PLAYER_ATTACK_DAM: punch_dam, PLAYER_ATTACK_CHANCE: punch_attack_chance},
        {PLAYER_ATTACK_NAME: "shoot at them with bow", PLAYER_ATTACK_DAM: shoot_with_bow_dam, PLAYER_ATTACK_CHANCE: shoot_with_bow_attack_chance}
        ]
    #list the different enemys for hard fights
    enemytofight = [
        {ENEMY_NAME: "Wendigo", ENEMY_MAX_HEALTH: 500, ENEMY_ATTACK_NAME: "slashes at you with supernatural speed ", ENEMY_DAMAGE: 50, ENEMY_HIT_CHANCE: 90},
        {ENEMY_NAME: "Minotaur", ENEMY_MAX_HEALTH: 500, ENEMY_ATTACK_NAME: "charges at you", ENEMY_DAMAGE: 50, ENEMY_HIT_CHANCE: 80},
        {ENEMY_NAME: "cerberus", ENEMY_MAX_HEALTH: 500, ENEMY_ATTACK_NAME: "bites you with its three heads", ENEMY_DAMAGE: 50, ENEMY_HIT_CHANCE: 70}
        ]
    #randomly chosing an boss
    chosen_enemy = random.choice(enemytofight)
    chosen_enemy_current_health = chosen_enemy[ENEMY_MAX_HEALTH]

    #telling you what boss is there and telling you your attacks
    print(f"you walked into the room and a {chosen_enemy[ENEMY_NAME]} is there \n get ready to fight")
    print(f"you have {your_current_health} health")
    while True:
        while True: 
            print("here are you attacks please answer in numbers")
            for i,j in enumerate(user_attacks):
                print(f"{i + 1}. {j[PLAYER_ATTACK_NAME]} damage is {j[PLAYER_ATTACK_DAM]}. Hit chance is {j[PLAYER_ATTACK_CHANCE]}")
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
        #telling you what attack the boss used 
        print(f" {chosen_enemy[ENEMY_NAME]}  {chosen_enemy[ENEMY_ATTACK_NAME]}")
        #getting the values for your attacks
        user_pick -= 1
        you_attack_chance = random.uniform(1,100)
        #seeing if you hit the boss and if so taking away some of its health
        if you_attack_chance < user_attacks[user_pick][PLAYER_ATTACK_CHANCE]:
            chosen_enemy_current_health -= user_attacks[user_pick][PLAYER_ATTACK_DAM]
            print(f"you hit the {chosen_enemy[ENEMY_NAME]} and did {user_attacks[user_pick][PLAYER_ATTACK_DAM]} damage. The {chosen_enemy[ENEMY_NAME]} has {chosen_enemy_current_health} health left")
        else: 
            print("you missed")
        if chosen_enemy_current_health <= 0:
            print(f"good job you beat the {chosen_enemy[ENEMY_NAME]}")
            print("you have manged to escape the dungeon and make it out")
            print("\n -------------------------------------------------")
            sys.exit()
        #seeing if the boss hit you and taking away your health
        enemy_attack_chance = random.uniform(1,100)
        if enemy_attack_chance < chosen_enemy[ENEMY_HIT_CHANCE]:
            your_current_health -= chosen_enemy[ENEMY_DAMAGE]
            print(f"you have {your_current_health} left")
        else:
            print(f"the {chosen_enemy[ENEMY_NAME]} missed")
        #cheaking if you die
        if your_current_health <= 0:
            print("I thought you would of been stronger given that you made it though my subordinates must of just been luck")
            sys.exit()
        print("\n -------------------------------------------------")
    
 #making the main loop
 
def main(number_of_times_though, bludgeon_dam , bludgeon_attack_chance , shiv_dam, shiv_attack_chance, punch_dam , punch_attack_chance , shoot_with_bow_dam , shoot_with_bow_attack_chance , your_current_health  ):   
    while number_of_times_though <= 15:
        rooms = [
            {KEY_NAME_ROOM:" big room", KEY_DISCRIPTION:"the exit on the other side has bars on it"},
            {KEY_NAME_ROOM:"a small room", KEY_DISCRIPTION:"has an anvil in the middle of it"},
            {KEY_NAME_ROOM:"a very big room", KEY_DISCRIPTION:"looks like there is something diffferent about it"},
            {KEY_NAME_ROOM: "A median room", KEY_DISCRIPTION:"An fountain stands in the middle "},
            {KEY_NAME_ROOM: "A median room",KEY_DISCRIPTION:"An altar stands in the middle" }
            ]
        chosen_room1 = random.choice(rooms)
        chosen_room2 = random.choice(rooms)
        while True:
            which_room = input(f"what room do you want to pick \n 1.{chosen_room1[KEY_NAME_ROOM]} - {chosen_room1[KEY_DISCRIPTION]} \n 2.{chosen_room2[KEY_NAME_ROOM]} - {chosen_room2[KEY_DISCRIPTION]} \n")
            try:
                which_room = int(which_room)
                if which_room > 2:
                    print("invild answer")
                    continue 
                else:
                    break
            except:
                print("invaild answer")
                continue 
            
        if which_room == 1:
            
            if chosen_room1[KEY_DISCRIPTION] == rooms[0][KEY_DISCRIPTION]:
                #calling fight room
                print("\n -------------------------------------------------")
                your_current_health = fight_room(your_current_health, bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance)
                number_of_times_though += 1
                continue 
            elif chosen_room1[KEY_DISCRIPTION] == rooms[1][KEY_DISCRIPTION]:
                #calling upgrade room
                number_of_times_though += 1
                print("\n -------------------------------------------------")
                bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance = upgrade_room(bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance)
    
            elif chosen_room1[KEY_DISCRIPTION] == rooms[2][KEY_DISCRIPTION]:
                # CALLing hard fight ROOM
                number_of_times_though += 1
                print("\n -------------------------------------------------")
                your_current_health = hard_fight_room(your_current_health, bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance)
                while True:
                    hard_fight_upgrade = input("now that the enemy is gone you see a small room do you want to go in yes/no").strip().upper()
                    if hard_fight_upgrade in ("YES","Y"):
                        #calling upgrade room as a reward 
                        bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance = upgrade_room(bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance)
                        break
                    elif hard_fight_upgrade in ("NO","N"):
                        print("you leave the room and on to the next one")
                        break
                    else:
                        print("invaild answer")
                        continue
            elif chosen_room1[KEY_DISCRIPTION] == rooms[3][KEY_DISCRIPTION]:
                #calling health room
                number_of_times_though += 1
                print("\n -------------------------------------------------")
                your_current_health = health_room(your_current_health)
            elif chosen_room1[KEY_DISCRIPTION] == rooms[4][KEY_DISCRIPTION]:
                #calling gambling room 
                number_of_times_though += 1
                print("\n -------------------------------------------------")
                your_current_health = gambling_health_room(your_current_health)
        #cheaking what they room they want 
        elif which_room == 2:
            
            if chosen_room2[KEY_DISCRIPTION] == rooms[0][KEY_DISCRIPTION]:
                print("\n -------------------------------------------------")
                your_current_health = fight_room(your_current_health, bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance)
                number_of_times_though += 1
                continue
            
            elif chosen_room2[KEY_DISCRIPTION] == rooms[1][KEY_DISCRIPTION]:
                #calling upgrade room
                number_of_times_though += 1
                print("\n -------------------------------------------------")
                bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance = upgrade_room(bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance)
            elif chosen_room2[KEY_DISCRIPTION] == rooms[2][KEY_DISCRIPTION]:
                # CALLing hard fight ROOM
                number_of_times_though += 1
                your_current_health = hard_fight_room(your_current_health, bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance)
                print("\n -------------------------------------------------")
                while True:
                    hard_fight_upgrade = input("now that the enemy is gone you see a small room do you want to go in yes/no").strip().upper()
                    if hard_fight_upgrade in ("YES","Y"):
                        #calling upgrade room as a reward 
                        bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance = upgrade_room(bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance)
                        break
                    elif hard_fight_upgrade in ("NO","N"):
                        print("you leave the room and on to the next one")
                        break
                    else:
                        print("invaild answer")
                        continue
                
            elif chosen_room2[KEY_DISCRIPTION] == rooms[3][KEY_DISCRIPTION]:
                #calling health room
                number_of_times_though += 1
                print("\n -------------------------------------------------")
                your_current_health = health_room(your_current_health)
            elif chosen_room2[KEY_DISCRIPTION] == rooms[4][KEY_DISCRIPTION]:
                #calling gambling room 
                number_of_times_though += 1
                print("\n -------------------------------------------------")
                your_current_health = gambling_health_room(your_current_health)
    print("\n -------------------------------------------------")
    print("you have made it to the final room before the exit")
    print("good luck beating the boss")
    print("\n -------------------------------------------------")
    boss_fight(your_current_health, bludgeon_dam, bludgeon_attack_chance, shiv_dam, shiv_attack_chance, punch_dam, punch_attack_chance, shoot_with_bow_dam, shoot_with_bow_attack_chance)
    
#calling the main code

main(number_of_times_though, bludgeon_dam , bludgeon_attack_chance , shiv_dam , shiv_attack_chance, punch_dam , punch_attack_chance , shoot_with_bow_dam , shoot_with_bow_attack_chance , your_current_health )


