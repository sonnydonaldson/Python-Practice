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

#getting there name

name = input("Hello what is your name ").capitalize()
print(f"hello {name}")




#seeing what rollercoster they want to go on


answer_vaild = False
while answer_vaild == False:
        #getting there hight and age
    height = input("how tall are you in centimeters ")
    height = int(height)
    age = input("what is your age ")
    age = int(age)


    #seeing if the have a heart condtion
    answer_vaild = False
    while answer_vaild == False:
        heart_condition = input("Do you have a heart condition ")

        if heart_condition.upper().strip() == "YES":
            heart_condition = True
            answer_vaild =  True
        elif heart_condition.upper().strip() == "NO": 
            heart_condition = False
            answer_vaild = True

    #seeing if the have a vip pass
    answer_vaild = False
    while answer_vaild == False:
        vip_pass = input("Do you have a VIP pass ")
        if vip_pass.upper().strip( ) == "YES":
            vip_pass = True
            answer_vaild = True
        elif vip_pass.upper().strip() == "NO": 
            vip_pass = False
            answer_vaild = True
        

        # seeing which rollercoster they want to go on 
        print("There are four roller costers to chose from\n pride before\n orphan maker\n I laughed as you fell\n normal boring rollercoster")
        which_rollercost = input("which one do you want to go on ").strip().upper()

        #telling them which rollercoster they can go on 
        if which_rollercost == "NORMAL BORING ROLLERCOSTER" and height > 150 and age > 10 and heart_condition == False or which_rollercost == "NORMAL BORING ROLLERCOSTER" and vip_pass == True : 
            print(f"You are allowed on the ride, go ahead {name}")
            answer_vaild == True
        elif which_rollercost == "NORMAL BORING ROLLERCOSTER" and not height > 150 or age > 10 or heart_condition == True :
            print(f"You are not allowed on the ride {name}")
            answer_vaild == True
        elif which_rollercost == "ORPHAN MAKER" and height > 180 and age > 31 and heart_condition == False or which_rollercost == "ORPHAN MAKER" and vip_pass == True:
            print(f"You are allowed on the ride, go ahead {name}")
            answer_vaild == True
        elif which_rollercost == "ORPHAN MAKER" and not height > 180 or age > 31 or heart_condition == True :
            print(f"You are not allowed on the ride {name}")
            answer_vaild == True
        elif which_rollercost == "I LAUGHED AS YOU FELL" and height > 50 and age > 3 and heart_condition == False  or which_rollercost == "I LAUGHED AS YOU FELL" and vip_pass == True:
            print(f"You are allowed on the ride, go ahead {name}")
            answer_vaild == True
        elif  which_rollercost == "I LAUGHED AS YOU FELL" and not height > 50 or age > 3 or heart_condition == True:
            print(f"You are not allowed on the ride {name}")
            answer_vaild == True
        elif answer_vaild == "PRIDE BEFORE" and height > 200 and age > 90 and heart_condition == False or answer_vaild == "PRIDE BEFORE" and vip_pass == True:
            print(f"You are allowed on the ride, go ahead {name}")
            answer_vaild == True
        elif  answer_vaild == "PRIDE BEFORE" and not height > 200 or age > 90 or heart_condition == True:
             print(f"You are not allowed on the ride {name}")
             answer_vaild == True








    """
    if height > 150 and age > 10 and heart_condition == False or vip_pass == True : 
        print(f"You are allowed on the ride, go ahead {name}")
    elif not height > 150 or age > 10 or heart_condition == True :
        print(f"You are not allowed on the ride {name}")
    """