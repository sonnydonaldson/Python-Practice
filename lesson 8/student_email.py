import random
# =====================================================================
# PROGRAM: Higher or Lower Number Guesser
# =====================================================================

# IMPORTS
# TODO: Import the 'random' module so you can generate a secret number.

# VARIABLES
# TODO: Generate a random number between 1 and 100 and save it to 'secret_number'.
# TODO: Create a variable to keep track of the user's current guess.
#       (Hint: Start it as 0 so it doesn't accidentally match the secret number!)


# INTRODUCE THE GAME
# TODO: Print a welcome message explaining that the number is between 1 and 100.


# START THE GAME
# TODO: Start a 'while' loop that keeps running AS LONG AS the 
#       user's guess is NOT EQUAL to the secret_number.

    
    # TODO: Ask the user to guess a number. 
    #       (CRITICAL HINT: Remember to convert their input into an integer!)


    # TODO: Create an 'if' statement to check if their guess is TOO LOW.
    #       If it is, print "Too low! Try a higher number."


    # TODO: Create an 'elif' statement to check if their guess is TOO HIGH.
    #       If it is, print "Too high! Try a lower number."


# GAME OVER / WINNING MESSAGE
# TODO: Print a big victory message telling them they got it right!

# ===========================================
# EXTENSION
# TODO: Create a play again option (you'll need to loop the whole code, including creating the random number)
# TODO: Add an extra condition that tells them if they are within 5 of the secret number

# ===========================================
# EXPERT
# TODO: Try to structure the program using defined functions


random_number = random.randint(1,100)
users_guess = 0 

print("hello this is a number guessing game the number is between 1 and 100")

while users_guess != random_number:
    users_guess = input("guess a random number")
    

