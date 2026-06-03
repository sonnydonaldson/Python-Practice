# =====================================================================
# Task: Country Guessing Game
# =====================================================================

# VALUES
# TODO: Create a variable to store the correct country (e.g., "Italy").
# TODO: Create a variable to keep track of the user's current guess. 
#       (Hint: Start it as an empty string "" so the loop runs at least once!)


# LOOP
# TODO: Start a 'while' loop. 
#       The loop should keep running AS LONG AS the user's guess 
#       is NOT EQUAL to the correct country.
    
    # TODO: Ask the user for their guess and save it to your guess variable.
    #       (Remember: This changes the loop condition so it doesn't run forever!)
    
    # TODO: (Optional) Add an 'if' statement inside the loop.
    #       If they guessed wrong, print an encouraging message or an extra hint.
    #       If they guessed right, the loop will automatically exit on the next check!


# GAME OVER / WINNING MESSAGE
# TODO: Print a congratulatory message celebrating their win!

# ================================================================
# EXTENSION
# TODO: Add an introduction
# TODO: Add a scoring system (starts at 20, lose 1 point for each wrong guess)
# TODO: Add a lose condition (if score reaches 0)

#==================================================================
# EXPERT
# TODO: Make the game unique (use a list of countries and randomly select one)
# TODO: Add a play again option


import random


correct = "italy","new zealand", "vatican city", "angola", "australia", "cuba" , "finland", "iceland", "israel" , "uzbekistan"
country = random.choice(correct)
person_guess = ""
score = 20
print("hello this is a game about guessing a country good luck")
print("there is also a scoring system and you lose one point for every time you guess wrong")
while person_guess != country:
    person_guess = input("what is your guess ").strip().lower()
    if person_guess != country:
        print("incorrect try again")
        score -= 1
if score > 0:
    print(f"you lose your score was {score}")
else:
    print("good job you got it right")
    print(f"your score is {score}")

