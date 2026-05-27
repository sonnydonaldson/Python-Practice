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


name = input("Hello what is your name ").capitalize()
print(f"hello {name}")



height = input("how tall are you in centimeters ")
height = int(height)
age = input("what is your age ")
age = int(age)



answer_vaild = False
while answer_vaild == False:
    heart_condition = input("Do you have a heart condition ")

    if heart_condition.upper().strip() == "YES":
        heart_condition = True
        answer_vaild =  True
    elif heart_condition.upper().strip() == "NO": 
        heart_condition = False
        answer_vaild = True


answer_vaild = False
while answer_vaild == False:
    vip_pass = input("Do you have a VIP pass ")
    if vip_pass.upper().strip( ) == "YES":
        vip_pass = True
        answer_vaild = True
    elif vip_pass.upper().strip() == "NO": 
        vip_pass = False
        answer_vaild = True
   



if height > 150 and age > 10 and heart_condition == False or vip_pass == True : 
    print(f"You are allowed on the ride, go ahead {name}")
elif not height > 150 and age > 10 and heart_condition == False :
    print(f"you are not allowed on the ride {name}")