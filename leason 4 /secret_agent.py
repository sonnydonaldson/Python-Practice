### Secret Agent Login
# Create a login process for a secret agent

# Ask for the user's name and save it in a variable

# Ask for the password and save it in a variable

# Check if the password == 'Falcon'

    # Ouput that access has been granted and welcome user using their name

    # Ask for the user's age and save it in a variable

    # Change the age into an integer

    # If the user's age is under 13, tell them they are a spy in training

    # If their age is under 18, tell them they are a junior spy

    # If their age is 18 or over, tell them they are a Field Agent

# Output a goodbye

# ___________________________

# EXTENSION

# Ask more questions to give your spy more information
# Look up how to use 'and' and 'or' to force more conditions (eg. they must be one of 3 users AND get the password correct)

# ___________________________

# EXPERT (For those who already know python)

# Create a SPY ID GENERATOR
# Your user must login using the correct password to access the generator
# Use a bunch of questions to generate an id. Eg. If their name has 4 or fewer letters, their ID is a random fruit plus other logic...\


# check for password and getting there name 
name = input("What is your name ").capitalize()
login_answer = input("What is the password ")


# repilying to the password 
if login_answer == ("Falcon"):
    print("Access has been granted, welcome " + name)
    person_name = input("What is your age spy ")
    person_name = int(person_name)
    if person_name < 13:
        print("You are a spy in training")
    if person_name < 18:
        print("you are a junior spy")
    if person_name >= 18:
        print("you are a full Field Agent good job")
    print("goodbye")

if login_answer != ("Falcon"):
    print("Incorrect")