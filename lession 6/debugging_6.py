import sys 
#giving their member status
MEMBER_STATUS = "gold"
#getting set row and conveting it
passenger_row = input("Enter your seat row: ")
passenger_row = int(passenger_row)
#cheaking if their ticket is valid and 
has_ticket = input("Do you have a valid ticket? (yes/no): ")
if has_ticket.lower() == "no":
    print("Access Denied. Please ensure you have a valid ticket before boarding.")
    sys.exit()

#giving them there status for boarding
if passenger_row <= 8 and MEMBER_STATUS == "gold":
    print("Welcome to priority boarding! Please make your way on board now.")

elif passenger_row <= 8 or MEMBER_STATUS == "gold":
    print("Welcome to priority boarding! Please wait for our Gold Business Flyers to finish boarding.")
else:
    passenger_row > 8 
    print("Please wait for general boarding.")

#getting their disternation and outputting their flight time 
destination = input("Enter your destination code: ").upper().strip()
if destination == "AKL" or destination == "WLG":
    print("Flight is delayed 5 minutes.")
elif destination == "CHC":
    print("flight is on time.")
else:
    print("Flight has been cancelled.")


# PSEUDOCODE START
# IF NOT destination is equal to "CHC" THEN print "Flight is on time."
# ELSE print "Flight has been cancelled"