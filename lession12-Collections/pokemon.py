# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================

# TODO Import random module

# Wild Pokemon
# TODO Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
# User Pokemon
# TODO Create a multidimensional list that holds 4 pokemon attacks and their different damage

# TODO Create a variable to hold a randomised wild pokemon
# TODO Create a current_health variable and set it to the max health of the random pokemon
# TODO Tell the user what pokemon they're facing
# TODO Create a while loop that continues until current health <= 0
    # TODO Ask the user which attack they'd like to use (list all 4 options, numbered); save input
    # TODO Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    # TODO Using the number, get the attack damage value and minus it from current health

# TODO Tell the user they defeated the pokemon

# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dictionary of strengths and weaknesses. Use this to change the damage
KEY_NAME = "name"
KEY_BASE_DAMAGE = "DAMAGE"
KEY_ATTACK_CHANCE = "HIT CHANCE"
MAX_HEALTH = "max health"
KEY_CRIT_CHANCE ="crit chance"
import random
Wild_Pokemon = [
    {KEY_NAME:"Rotom",MAX_HEALTH: 50},
    {KEY_NAME:"Mewtwo", MAX_HEALTH: 106},
    {KEY_NAME:"Eternatus", MAX_HEALTH: 140},
    {KEY_NAME: "Diglett", MAX_HEALTH: 10}
]
User_Pokemon_atttack = [
    {KEY_NAME: "beak blast",KEY_BASE_DAMAGE: 85, KEY_ATTACK_CHANCE : 100, KEY_CRIT_CHANCE: 1},
    {KEY_NAME :"fire blast",KEY_BASE_DAMAGE :120, KEY_ATTACK_CHANCE : 85,KEY_CRIT_CHANCE: 1},
    {KEY_NAME : "vine wip",KEY_BASE_DAMAGE : 45, KEY_ATTACK_CHANCE: 100,KEY_CRIT_CHANCE: 1},
    {KEY_NAME:"Fissure", KEY_BASE_DAMAGE: 10000, KEY_ATTACK_CHANCE: 30,KEY_CRIT_CHANCE: 0}
]
randomised_wild_pokemon = random.choice(Wild_Pokemon)
current_health = randomised_wild_pokemon[MAX_HEALTH]
print(f"you are facing {randomised_wild_pokemon[KEY_NAME]}")

while current_health >= 0:
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
    attack_chance = random.uniform(1,100)
    crit_chance = 1
    user_pick -= random.uniform(1,24)
    if attack_chance <= User_Pokemon_atttack[user_pick][KEY_ATTACK_CHANCE]:  
        if crit_chance == User_Pokemon_atttack[user_pick][KEY_CRIT_CHANCE]:
            print("you crit")
            hit_dmage = User_Pokemon_atttack[user_pick][KEY_BASE_DAMAGE] * 1.5
        hit_dmage = User_Pokemon_atttack[user_pick][KEY_BASE_DAMAGE]
        current_health -= hit_dmage
        print("you hit")
    else:
        print(f"you missed the {randomised_wild_pokemon[KEY_NAME]}")
    print(f"the {randomised_wild_pokemon[KEY_NAME]} has {current_health} health left")
print(f"Good job you beat {randomised_wild_pokemon[KEY_NAME]}")