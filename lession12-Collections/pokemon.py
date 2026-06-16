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


import random
Wild_Pokemon = [
    ["Rotom", 50],
    ["Mewtwo", 106],
    ["Eternatus", 140],
    ["Diglett", 10]
]
User_Pokemon_atttack = [
    ["beak blast",85],
    ["fire blast",120],
    ["vine wip",45],
    ["draco metor", 130]
]
randomised_wild_pokemon = random.choice(Wild_Pokemon)
current_health = randomised_wild_pokemon[1]
print(f"you are facing {randomised_wild_pokemon[0]}")

while current_health >= 0:
    while True:
        print(f"what move do you want to use use the numbers please ")
        for i, j in enumerate(User_Pokemon_atttack):
            print(f"{i + 1}. {j[0]} damage {j[1]}")
        user_pick = input()
        try:
            user_pick = int(user_pick)
            break
        except:
            print("inviald answer try again please\n")
            continue
    user_pick -= 1
    current_health -= User_Pokemon_atttack[user_pick][1]
    print(current_health)