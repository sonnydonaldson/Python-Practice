# Create a calculator that asks the user for a number (of days)
# and outputs how many seconds in that number of days

# Values - start by writing constants to hold:
# The number of seconds in a minute

# The number of minutes in an hour

# The number of hours in a day


# Get input from the user and save it in a variable

# Change the value into an integer and resave in the variable


# Calculate the number of seconds using * with the input and your constants. 
# Save it in a new variable.

# Output the answer

# ---------------------------------

# EXTENSION
# Also output how many total hours and how many total minutes in the days
# Create another calculator that does the opposite (input is seconds, output is days)

# ---------------------------------

# EXPERT (for those who already know some Python)
# Create the calculator above, but...
#   allow your user to choose the input and output type (seconds, minutes, hours, days)
#   Loop the calculator so they can do it again with having to reopen the program.


NUMBER_OF_SECONDS_IN_MINUTE = 60

NUMBER_OF_MINUTES_IN_A_HOUR = 60

NUMBER_OF_HOURS_IN_DAY = 24


print("How many seconda in a X amout of days calculator")
number_of_days = input("How many days\n")
day_in_interger = int(number_of_days)
answer_seconds = (day_in_interger * NUMBER_OF_HOURS_IN_DAY * NUMBER_OF_MINUTES_IN_A_HOUR * NUMBER_OF_SECONDS_IN_MINUTE)
answer_minutes = (day_in_interger * NUMBER_OF_HOURS_IN_DAY * NUMBER_OF_MINUTES_IN_A_HOUR)
answer_hours = ( day_in_interger * NUMBER_OF_HOURS_IN_DAY)
print("the answer to the question in seconds is " + str(answer_seconds))
print("the answer to the question in minutes is " + str(answer_minutes ))
print("the answer to the question in hours is " + str(answer_hours))

