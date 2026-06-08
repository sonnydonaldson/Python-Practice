# =====================================================================
# PROGRAM: Safe Cracker (The Digital Vault)
# =====================================================================

# SETUP YOUR VARIABLES
# TODO: Create a variable for the correct vault combination (e.g., "742").
# TODO: Create a variable to keep track of how many attempts the player has used (start at 0).


# INTRODUCE THE GAME
# TODO: Print a cool message explaining they are trying to hack a safe.
# TODO: Let them know that typing 'exit' will quit the game entirely.


# LOOP
# TODO: Create an infinite while loop
# Note: By using 'True', this loop will run forever unless we use 'break'!

    # TODO: Ask the user to enter the 3-digit combination (or type 'exit').
    #       Save their input into a variable called 'user_input'.


    # -----------------------------------------------------------------
    # SCENARIO A: The user wants to quit
    # -----------------------------------------------------------------
    # TODO: Check if 'user_input' is equal to the word 'exit'.
    #       If it is, print "Aborting mission..." and use 'break' to stop the loop!


    # -----------------------------------------------------------------
    # SCENARIO B: Invalid Input
    # -----------------------------------------------------------------
    # TODO: Check if their input is a valid number
    #       (Hint: use try except)
    #       If it's not, print "Error: Safe only accepts digits. Try again."
    #       Then, use 'continue' to skip the rest of the code and restart the loop.


    # -----------------------------------------------------------------
    # SCENARIO C: Processing a valid attempt
    # -----------------------------------------------------------------
    # If the code gets past Scenario B, it means they entered a valid 3-digit attempt!
    
    # TODO: Increase your attempts tracker variable by 1.


    # TODO: Check if 'user_input' matches the correct vault combination.
    #       If it does: Print "Vault unlocked! You found the treasure!" and 'break' out of the loop.
    #       If it doesn't: Print a message telling them the comination failbed.


# GAME OVER
# ---------------------------------------------------------------------




# =========================================
# EXTENSION
# TODO Add a scenario D to your loop: Running out of time
    # -----------------------------------------------------------------
    # SCENARIO D: Running out of time (EXTENSION)
    # -----------------------------------------------------------------
    # TODO: Check if their attempts tracker has reached 5.
    #       If it has, print "Alarm triggered! Security is on the way!" and 'break' the loop.

# =========================================
# EXPERT
# Mastermind Version:
# Add a part that lets you check each digit (you'll need to use split()) and tells the user how many digits are correct in their guess

correct_combernation = 325
how_many_attempts = 0

print("you are trying to hack a safe good luck theif")
print("by the way if you type exit it will end it")

while True:
    user_input = input("what is the three digit combernation ").strip().lower()
    if user_input == "exit":
        print("Aborting mission...")
        break
    try:
        user_input = int(user_input)
    except:
        print("Error: Safe only accepts digits. Try again.")
        continue
    how_many_attempts += 1
    if how_many_attempts == 5:
        print("Alarm triggered! Security is on the way you failed")
        break
    if user_input == correct_combernation:
        print(f"Vault unlocked! You found the treasure! it took you {how_many_attempts} trys")
        break
    else:
        print("comination failed try again ")
