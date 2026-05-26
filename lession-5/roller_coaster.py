# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input





# Check conditions and output verdict




# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient
name = input("Hello what is your name ")
print(f"hello {name}")

height = input("how tall are you in centimeters ")
height = int(height)
age = input("what is your age ")
age = int(age)
heart_condition = input("Do you have a heart condition ")
vip_pass = input("Do you have a VIP pass")


if heart_condition.upper() == "YES":
    heart_condition = True
elif heart_condition.upper() == "NO": 
    heart_condition = False



if height > 150 and age > 10 and heart_condition == False or vip_pass == True : 
    print("You are allowed on the ride go ahead")
