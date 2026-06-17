"""
PROGRAM: Geometry Helper
This program helps to calculate the area and circumference of a rectangle
"""

####### INSTRUCTIONS ########
# Complete the code by writing a function for calculating the circumference, 
# and calling each calculate function based on user choice


# =====================================================================
# FUNCTIONS
# =====================================================================

# Calculate the area of a rectangle based on length and width from user
def calculate_area():
    length = int(input("What is the length?"))
    width = int(input("What is the width?"))
    print(f"The area is {length * width }².")


# TODO ------->>>> Write a function here for calculating the parameter after getting length and width from user

def calculate_parameter():
    length = int(input("What is the length?"))
    width = int(input("What is the width?"))
    print(f"the parameter is {(length + width) * 2 }")
    
# Run the main program
def main():

    print("Welcome to the Geometry Helper for rectangles!\n")
    print("1. Area Calculator")
    print("2. Parameter Calculator")

    choice = input("\nWhich tool do you want to use? (1 or 2): ").strip()

    # Trigger function based on user choice
    if choice == "2":
        calculate_parameter()
        # TODO ------->>>> Call the function for calculating area here

    elif choice == "1":
        calculate_area()
        # TODO ------->>>> Call the function for calculating circumference here

    else:
        print("Invalid choice. Exiting dashboard.")


# =====================================================================
# EXECUTION
# =====================================================================
main()