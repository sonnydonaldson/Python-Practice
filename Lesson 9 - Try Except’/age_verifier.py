# =====================================================================
# PROGRAM: Age verification
#           Verify the user's age is over 18 to give access (or deny access)
#           Keep asking for input until they've given a valid age
# =====================================================================

# VARIABLES
# TODO Create a variable for valid input and set it to false

# GET INPUT
# TODO Start a loop while the input is invalid

    # TODO Ask the user for their age and save it

    #TRY
    # TODO Create a try statement
        # TODO Change the input into an integer and resave it
        # TODO Set the valid input variable to true

    # FAIL TO CONVERT TO INTEGER
    # TODO Add an except statement
    # TODO Tell the user their input was invalid

# Unindented = Loop has finished so the input must be valid now

# CHECK AGE
# TODO Check if they are older than 18 and tell them they have access if they are
# TODO Check if they are older than 13 and tell them they have partial access if they are.
# TODO Otherwise tell them access has been denied


# ===================================================================
# EXTENSION
# Create a avatar creator for them to use if they get access. There should be 2 versions (full and partial)
# Eg. Full can choose: character class (warrior, rogue), hair colour, eye colour; partial just character class (with animal classes?)

valid_input = False

while valid_input == False:
    user_age = input("what is your age \n ")
    try:
        user_age = int(user_age)
        valid_input = True
    except:
        print("your input was invaild")
        valid_input = False

if user_age < 13:
    print("access denied")
elif user_age > 13 and user_age < 18:
    print("you have partial access")
    classs = input("what class do you want to choose \n warrior \n rogue \n mage \n tank \n")
    access = "partial access"
    full_access_insttions = ""
else:
    print("you have full access")
    classs = input("what class do you want to choose \n warrior \n rogue \n mage \n tank \n")
    hair_color = input("what hair color do you want\n").lower().strip()
    eye_color = input("what eye color do you want \n").lower().strip()
    access = "full access"
    full_access_insttions = (f"and your hair color is {hair_color} with your eyes being {eye_color}")
print(f"you are {classs} class and you have {access} {full_access_insttions}")