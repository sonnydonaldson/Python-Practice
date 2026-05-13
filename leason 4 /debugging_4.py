#printing the starting thinf and getting how many steps they did
print("--- Daily Step Tracker ---")
steps = input("How many steps did you walk today? ")

# convetting it do be abkle to conpare it 
steps = int(steps)
#compareing it to the vaules and outputing the answer 
if steps > 10000:
    print("Amazing! You walked over 10,000 steps! You are a Pro Athlete.")
if steps < 5000:
    print("Good start, but try to walk a bit more tomorrow!")

#doing the stuff for daily goal and checking if they did it or not 
DAILY_GOAL = 5000

if steps == DAILY_GOAL:
    print("Bullseye! You hit your goal exactly!")

# seeing if the got any steps at all
if steps == 0:
    print("Did you forget your phone today? You have 0 steps")
print("Tracker closing...")


