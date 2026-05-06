import sys 
# Create a short Madlib: Get input from your user (a bunch of words), 
# then output a madlib using those words.

# Ask user for a name and save it in a variable

# Ask user for an animal and save it in a variable

# Ask user for a colour and save it in a variable

# Ask user for an object and save it in a variable

# Print your madlib using the 4 variables above.

# ----------------------------

# EXTENSION
# Research about 'print formatting in python'. 
# Use what you learn to rewrite your madlib into easier to read code.

# ----------------------------

# EXPERT (for those who already know some Python)
# Create a randomised madlib game
# GOAL: Just like above except...
#       Write 4-6 different madlibs and randomise which one is output.


 
name = input("what is your name?\n").capitalize()
if name in ("Noah", "Lief", "Beau", "Ethan", "Ryder", "Gigi", "Arlo", "Conner", "Ashton") : 
    print("fuck you " + name + " go away") 
    sys.exit()
elif name in ("Cole", "John"):
    name = "God"
favourite_animal = input("what is your favourite animal " + name + "\n").capitalize()
favourite_color = input("what is your favourite color " + name + "\n")
object = input("give me a random object you like "+ name + "\n")

print("hello "+name +" your favourite animal is " +favourite_animal +" and your favourite color is " +favourite_color+" and an object you like is a "+object)