# Create a student email creator that uses first and lat name plus id
# eg. smithjohn123@fake.school.nz

# Get input (first, last, id) and save in variables

# Strip input to remove accidental spaces and turn names into lowercase (resave in variables)




# Output the final email address

# --------------------------------

# EXTENSION
# Create a temporary password to output as well
# It should be their names in all uppercase and their id divided by 10

# --------------------------------

# EXPERT
# Create a WSCW email creator
# Get the users first and last name, then randomly generate an ID number (8 digits long)
# Output the email addess (lastf.wsc.school.nz) 
# - you'll need to strip down the first name to just first letter
# Output their id number
# Output a temporary password (all uppercase). You can choose how you create this, 
# but it needs to be unique for each user










print("Hello this is a student email creator")
first_name = input("what is your first name ").lower().strip()
last_name = input("what is your last name ").lower().strip()
id = input("give me some numbers ").lower().strip()

first_name_password = first_name.upper()
last_name_password = last_name.upper()
id_password = float(id)/10
id_password = str(id_password)



print("This is your email\n"+ first_name + last_name + id +"@gmail.com")
print("Here is a temorary password a]s well\n" + first_name_password + last_name_password + id_password)