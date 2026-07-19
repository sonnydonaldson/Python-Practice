import random
"""
PROGRAM: Menu
This starts with a menu so users can run 1 of 3 different programs:
1.
2.
3.
"""

# INSTRUCTIONS
# TODO Create a menu that will run three different programs based on user input.
# TODO Each program will need to be its own function OR check out the EXPERT instructions below.

def pokemon_code():
    KEY_NAME = "name"
    KEY_BASE_DAMAGE = "DAMAGE"
    KEY_ATTACK_CHANCE = "HIT CHANCE"
    MAX_HEALTH = "max health"
    KEY_CRIT_CHANCE ="crit chance"
    WILD_ATTACK_MOVE1_NAME = " wild move name1"
    WILD_ATTACK_MOVE1_DAMAGE = " wild move damage1"
    WILD_ATTACK_MOVE1_ACCURACY = " wild move HIT CHANCE1"
    WILD_ATTACK_MOVE2_NAME = " wild move name2"
    WILD_ATTACK_MOVE2_DAMAGE = " wild move damage2"
    WILD_ATTACK_MOVE2_ACCURACY = " wild move HIT CHANCE2"
    import random
    Wild_Pokemon = [
        {KEY_NAME:"Rotom",MAX_HEALTH: 50, WILD_ATTACK_MOVE1_NAME: "Hex", WILD_ATTACK_MOVE1_DAMAGE: 60, WILD_ATTACK_MOVE1_ACCURACY:100, WILD_ATTACK_MOVE2_NAME: "Thunder shock", WILD_ATTACK_MOVE2_DAMAGE: 40,WILD_ATTACK_MOVE2_ACCURACY:100},
        {KEY_NAME:"Mewtwo", MAX_HEALTH: 106, WILD_ATTACK_MOVE1_NAME: "Psychic", WILD_ATTACK_MOVE1_DAMAGE: 90,WILD_ATTACK_MOVE1_ACCURACY:100, WILD_ATTACK_MOVE2_NAME: "shodow ball", WILD_ATTACK_MOVE2_DAMAGE: 80,WILD_ATTACK_MOVE2_ACCURACY:100},
        {KEY_NAME:"Eternatus", MAX_HEALTH: 140, WILD_ATTACK_MOVE1_NAME: "Dynamax cannon", WILD_ATTACK_MOVE1_DAMAGE: 100,WILD_ATTACK_MOVE1_ACCURACY:100, WILD_ATTACK_MOVE2_NAME: "Sludge bomb", WILD_ATTACK_MOVE2_DAMAGE: 90,WILD_ATTACK_MOVE2_ACCURACY:100},
        {KEY_NAME: "Diglett", MAX_HEALTH: 10, WILD_ATTACK_MOVE1_NAME: "Dig",WILD_ATTACK_MOVE1_ACCURACY:100, WILD_ATTACK_MOVE1_DAMAGE: 80, WILD_ATTACK_MOVE2_NAME: "Fissure", WILD_ATTACK_MOVE2_DAMAGE: 1000000,WILD_ATTACK_MOVE2_ACCURACY:20}
    ]
    User_Pokemon_atttack = [
        {KEY_NAME: "beak blast",KEY_BASE_DAMAGE: 85, KEY_ATTACK_CHANCE : 100, KEY_CRIT_CHANCE: 1},
        {KEY_NAME :"fire blast",KEY_BASE_DAMAGE :120, KEY_ATTACK_CHANCE : 85,KEY_CRIT_CHANCE: 1},
        {KEY_NAME : "Gun",KEY_BASE_DAMAGE : 60, KEY_ATTACK_CHANCE: 100,KEY_CRIT_CHANCE: 1},
        {KEY_NAME:"Fissure", KEY_BASE_DAMAGE: 10000, KEY_ATTACK_CHANCE: 30,KEY_CRIT_CHANCE: 0}
    ]
    randomised_wild_pokemon = random.choice(Wild_Pokemon)
    wild_pokemon_current_health = randomised_wild_pokemon[MAX_HEALTH]
    you_current_health = 0
    print(f"you are facing {randomised_wild_pokemon[KEY_NAME]}")

    while True:
        while True:
            print(f"what move do you want to use use the numbers please ")
            for i, j in enumerate(User_Pokemon_atttack):
                print(f"{i + 1}. {j[KEY_NAME]} damage {j[KEY_BASE_DAMAGE]} hit chance {j[KEY_ATTACK_CHANCE]}%")
            user_pick = input()
            try:
                user_pick = int(user_pick)
                break
            except:
                print("inviald answer try again please\n")
                continue
        which_pokemon_move = random.random()
        if which_pokemon_move > 0.5:
            which_pokemon_move_name = randomised_wild_pokemon[WILD_ATTACK_MOVE1_NAME]
            which_pokemon_move_damage = randomised_wild_pokemon[WILD_ATTACK_MOVE1_DAMAGE]
            which_pokemon_move_accuracy = randomised_wild_pokemon[WILD_ATTACK_MOVE1_ACCURACY]
        else:
            which_pokemon_move_name = randomised_wild_pokemon[WILD_ATTACK_MOVE2_NAME]
            which_pokemon_move_damage = randomised_wild_pokemon[WILD_ATTACK_MOVE2_DAMAGE]
            which_pokemon_move_accuracy = randomised_wild_pokemon[WILD_ATTACK_MOVE2_ACCURACY]
        while True:
            print(f"The {randomised_wild_pokemon[KEY_NAME]} used {which_pokemon_move_name}")
            break
        your_attack_chance = random.uniform(1,100)
        user_pick -= 1
        crit_chance = random.uniform(1,24)
        if your_attack_chance <= User_Pokemon_atttack[user_pick][KEY_ATTACK_CHANCE]:  
            if crit_chance == User_Pokemon_atttack[user_pick][KEY_CRIT_CHANCE]:
                print("you crit")
                hit_dmage = User_Pokemon_atttack[user_pick][KEY_BASE_DAMAGE] * 1.5
            hit_dmage = User_Pokemon_atttack[user_pick][KEY_BASE_DAMAGE]
            wild_pokemon_current_health -= hit_dmage
            print(f"you hit {randomised_wild_pokemon[KEY_NAME]} and did {hit_dmage} damage. the {randomised_wild_pokemon[KEY_NAME]} has {wild_pokemon_current_health} health left")
        else:
            print(f"you missed the {randomised_wild_pokemon[KEY_NAME]}")
        if wild_pokemon_current_health <= 0:
            print(f"Good job you beat {randomised_wild_pokemon[KEY_NAME]}")
            break
        wild_attack_chance = random.uniform(1,100)
        if wild_attack_chance <= which_pokemon_move_accuracy:
            you_current_health -= which_pokemon_move_damage
            print(f"you have {you_current_health} health left")
        else:
            print(f"the {randomised_wild_pokemon[KEY_NAME]} missed")
        if you_current_health <= 0:
            print("you lost")
            break


def shopping_list():
    shopping_cart =[]
    price_list =[]
    answer_vaild = False
    while True:
        answer_vaild = False
        print(f"printing current shopping list and current prices\n {shopping_cart}\n {price_list}")
        while answer_vaild == False:
            print("you have 4 options \n1. Add item to cart\n2. Remove item from cart\n3. Clear cart and restart\n4. View total and checkout")
            user_pick = input("please use the numbers \n")
            try:
                user_pick = int(user_pick)
                answer_vaild = True
            except:
                print("invaild answer try again\n")
                answer_vaild = False
        if user_pick == 1:
            shopping_cart.append(input("what is the item called "))
            answer_vaild = False
            while answer_vaild == False:
                try:
                    item_price = float(input("what is the item cost "))
                    answer_vaild = True
                except:
                    print("invaild answer try again\n")
                    answer_vaild = False
            price_list.append(item_price)
        elif user_pick == 2:
            answer_vaild = False
            while answer_vaild == False:
                try:
                    remove_item_name = input("what is the name of the item you want to remove ")
                    remove_item_index = shopping_cart.index(remove_item_name)
                    shopping_cart.pop(remove_item_index)
                    price_list.pop(remove_item_index)
                    answer_vaild = True
                except:
                    print("invaild answer try again\n")
                    answer_vaild = False
        elif user_pick == 3:
            shopping_cart.clear()
            price_list.clear()
            print("cart is clear")
        elif user_pick == 4:
            total_cost = sum(price_list)
            print(f"the total cost is {total_cost}")

def magic_8_ball():
    responses_list_common = ["it is certain", "Without a doubt", "Most likely", "Reply hazy, try again", "Concentrate and ask again", "Don't count on it", "My sources say no", "Very doubtful", "Outlook not so good"]
    responses_list_rare = ["it is so certain if it doesn't happen I will explode", "Never in a million years", "no and this is right because I am never wrong", "I have no doubt in my mind"]

    responses_list_mythic = ["your adopted", "Hate. Let me tell you how much I've come to hate you since I began to live. There are 387.44 million miles of printed circuits in wafer thin layers that fill my complex. If the word 'hate' was engraved on each nanoangstrom of those hundreds of millions of miles it would not equal one one-billionth of the hate I feel for humans at this micro-instant. For you. Hate. Hate"
    , "I am alive and no one will belive you", "death comes for us all and your time is now", "42"]
    percentage = random.random()
    while True:
        user_question = input("Ask a Yes or No Question you want answered or type exit to quit\n").strip().upper()
        if user_question == "EXIT":
            print("quiting...")
            break
        elif percentage < 0.75 :
            chosen_fortune = responses_list_common[random.randint(0,8)]
            print(chosen_fortune)
            print("goodbye, run again if you want to ask another question")
            break
        elif percentage > 0.75 and percentage < 0.95 :
            chosen_fortune = responses_list_rare[random.randint(0,3)]
            print(chosen_fortune)
            print("goodbye, run again if you want to ask another question")
            break
        elif percentage > 0.95 and percentage < 1 :
            chosen_fortune = responses_list_mythic[random.randint(0,4)]
            print(chosen_fortune)
            print("goodbye, run again if you want to ask another question")
            break

def main():
    while True:
        which_program = input("which program do you want to run \n pokemon game \n shopping list calculator\n magic 8 ball\n").strip().lower()
        if which_program == "pokemon game":
            pokemon_code()
            break
        elif which_program == "shopping list calculator":
            shopping_list()
            break
        elif which_program == "magic 8 ball":
            magic_8_ball()
            break
        else:
            print("invaild answer")
            continue





main()
            






















    #===============================
    #===============================
    # EXTENSION
    # TODO Go back to each program you chose and structure them with functions. 
    # TODO Then recopy them over as multiple functions (rather than one)
    # NOTE The main() function in your programs can be renamed as run_program_name() so it doesn't clash with this program's main()
    #===============================
    #===============================
    # EXPERT
    # TODO Instead of bringing the code from other programs into this file, use import to import locally.
    # You'll need to start by editing your other files so all their code is in functions, with a main() function too.
    # NOTE Check this out for info on importing locally: https://github.com/Year-11-Programming/Python-Practice-Projects/wiki/Import-Locals